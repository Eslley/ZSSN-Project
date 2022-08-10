from django.urls import reverse
from urllib import response
from zssnapi.models.InventarioModel import InventarioModel
from zssnapi.models.ItemModel import ItemModel
from zssnapi.tests.test_setup import TestSetUp


class TestViews(TestSetUp):

    def test_sobrevivente_nao_pode_registrar_sem_dados(self):
        response = self.client.post(self.create_url)

        self.assertEqual(response.status_code, 400)

    def test_sobrevivente_nao_pode_registar_sem_inventario(self):
        response = self.client.post(self.create_url, self.sobrevivente_dados_sem_inventario)
        
        self.assertEqual(response.status_code, 400)

    def test_sobrevivente_cadastrar_corretamente(self):
        response = self.client.post(self.create_url, self.sobrevivente_dados_corretos, format='json')
        
        self.assertEqual(response.status_code, 201)

    def test_atualiza_localizacao_sobrevivente_corretamente(self):
        sobrevivente_localization = {
            "latitude": 5.1234567,
            "longitude": 42.1234567,
        }

        response = self.client.put(self.update_localization_url, sobrevivente_localization, format='json')

        self.sobrevivente.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.sobrevivente.latitude, 5.1234567)
        self.assertEqual(self.sobrevivente.longitude, 42.1234567)  

    def test_atualiza_localizacao_sobrevivente_sem_dados(self):
        sobrevivente_localization = {}

        response = self.client.put(self.update_localization_url, sobrevivente_localization, format='json')

        self.assertEqual(response.status_code, 400)

    def test_contabiliza_uma_sinalizacao_de_contaminacao(self):
        response = self.client.put(self.alert_contamination_url)

        self.sobrevivente2.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.sobrevivente2.countAlertInfected, 1)
        self.assertEqual(self.sobrevivente2.estaInfectado, False)

    def test_contabiliza_tres_sinalizacoes_de_contaminacao(self):

        self.alert_contamination_url = reverse('sobrevivente-infectado', kwargs={'info': self.sobrevivente.pk, 'cont': self.sobrevivente4.pk})
        response = self.client.put(self.alert_contamination_url)

        self.assertEqual(response.status_code, 200)

        self.alert_contamination_url = reverse('sobrevivente-infectado', kwargs={'info': self.sobrevivente2.pk, 'cont': self.sobrevivente4.pk})
        response = self.client.put(self.alert_contamination_url)

        self.assertEqual(response.status_code, 200)

        self.alert_contamination_url = reverse('sobrevivente-infectado', kwargs={'info': self.sobrevivente3.pk, 'cont': self.sobrevivente4.pk})
        response = self.client.put(self.alert_contamination_url)

        self.assertEqual(response.status_code, 200)

        self.sobrevivente4.refresh_from_db()

        self.assertEqual(self.sobrevivente4.countAlertInfected, 3)
        self.assertEqual(self.sobrevivente4.estaInfectado, True)

    def test_adicionar_item_com_pontos_menor_que_um(self):
        response = self.client.post(self.create_item_url, self.item_dados_incorretos)

        self.assertEqual(response.status_code, 400)

    def test_deletar_item(self):
        response = self.client.delete(self.delete_item_ulr)

        self.assertEqual(response.status_code, 200)