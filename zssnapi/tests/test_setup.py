from django.urls import reverse
from rest_framework.test import APITestCase
from zssnapi.models.ItemModel import ItemModel

from zssnapi.models.SobreviventeModel import SobreviventeModel

class TestSetUp(APITestCase):

    def setUp(self):

        self.sobrevivente = SobreviventeModel.objects.create(nome='Nanfred Junior', idade=22, sexo='m', latitude=5.0888877, longitude=42.999991)
        self.sobrevivente2 = SobreviventeModel.objects.create(nome='Dubov Francisco', idade=32, sexo='m', latitude=5.665334, longitude=42.0021333)
        self.sobrevivente3 = SobreviventeModel.objects.create(nome='Joanne Fay', idade=28, sexo='f', latitude=5.000022, longitude=42.0021113)
        self.sobrevivente4 = SobreviventeModel.objects.create(nome='Marsha', idade=42, sexo='f', latitude=5.885334, longitude=41.0023300)

        self.item = ItemModel.objects.create(nome="itemteste", pontos=9)

        self.item2 = ItemModel.objects.create(nome="itemteste2", pontos=5)
        self.item3 = ItemModel.objects.create(nome="itemteste3", pontos=4)

        self.create_url = reverse('sobrevivente-create')
        self.update_localization_url = reverse('sobrevivente-update-localization', kwargs={'pk': self.sobrevivente.pk})
        self.alert_contamination_url = reverse('sobrevivente-infectado', kwargs={'info': self.sobrevivente.pk, 'cont': self.sobrevivente2.pk})
        self.delete_item_ulr = reverse('item-delete', kwargs={'pk': self.item.pk})
        self.create_item_url = reverse('item-create')

        self.item_dados_incorretos = {
            "nome": "alimento",
            "pontos": -2
        }

        self.sobrevivente_dados_sem_inventario = {
            "nome": "Rubem Eslley",
            "idade": 20,
            "sexo": "m",
            "latitude": 5.037178,
            "longitude": 42.792717
        }

        self.sobrevivente_dados_corretos = {
            "nome": "Rubem Eslley",
            "idade": 20,
            "sexo": "m",
            "latitude": 5.037178,
            "longitude": 42.792717,
            "inventario": [
                {
                    "id": self.item2.pk,
                    "quantidade": 2
                    
                },
                {
                    "id": self.item3.pk,
                    "quantidade": 2
                }
            ]
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()