<template>
    
    <div class="container">

        <h4 class="center-align subtitle-page"><i class="material-icons">people</i> Sobreviventes</h4>

        <Message :msg="msg" v-show="msg" />

        <Loading :isLoading="isLoading"/>

        <form v-show="edit || add" action="#" @submit.prevent="">

            <div class="row">
                <div class="input-field col l10 s12">
                <label :class="{ active: edit }">Nome</label>
                <input :disabled="edit" type="text" v-model="sobrevivente.nome" >
                </div>
                
                <div class="input-field col l2 s12">
                <label :class="{ active: edit }">Idade</label>
                <input :disabled="edit" type="number" v-model="sobrevivente.idade" >
                </div>
            </div>

            <div class="row">
                <div class="col m1 s12">
                    <label>Sexo</label>
                </div>

                <div class="col m2 s16">
                    <label>
                        <input :disabled="edit" name="group1" type="radio" value="m" v-model="sobrevivente.sexo" />
                        <span>Masculino</span>
                    </label>
                </div>

                <div class="col m2 s6">
                    <label>
                        <input :disabled="edit" name="group1" type="radio" value="f" v-model="sobrevivente.sexo" />
                        <span>Feminino</span>
                    </label>
                </div>
            </div>

            <div class="row">
                <div class="col l6 s12">
                <label>Latitude</label>
                <input type="number" placeholder="Latitude" v-model="sobrevivente.latitude" >
                </div>

                <div class="col l6 s12">
                <label>Longitude</label>
                <input type="number" placeholder="Longitude" v-model="sobrevivente.longitude" >
                </div>
            </div>


            <label v-show="!edit" >Insira a quantidade de itens do sobrevivente</label>

            <table v-show="!edit" class="center">

                <thead>

                <tr>
                    <th>Item</th>
                    <th class="center-align">Pontos</th>
                    <th class="center-align">Quantidade</th>
                </tr>

                </thead>

                <tbody>

                    <tr v-for="(item, index) in itens" :key="item.id">

                        <td>{{ item.nome }}</td>
                        <td class="center-align"><span>{{ item.pontos }}</span></td>
                        <td class="td-input">
                            <input class="center-align" type="number" placeholder="Qtd" v-model="itens[index].quantidade" >
                        </td>

                    </tr>

                </tbody>
            
            </table>

            <div class="center-align save-button">
                <button @click="clear()" class="waves-effect waves-light btn-small">Fechar<i class="material-icons left">clear</i></button>
                <button @click="saveOrEdit()" class="waves-effect waves-light btn-small blue modal-trigger">Salvar<i class="material-icons left">save</i></button>
            </div>
      </form>

        <a @click="showForm()" v-show="!add && !edit" class="waves-effect waves-light btn"><i class="material-icons left">add</i>Adicionar</a>
      
      <table v-show="!add && !edit" class="center">

        <thead>

          <tr>
            <th>Id</th>
            <th>Nome</th>
            <!-- <th>Idade</th>
            <th>Sexo</th> -->
            <!-- <th>Latitude</th>
            <th>Longitude</th> -->
            <th class="center-align">Infectado</th>
            <th class="center-align">Alertas</th>

            <th class="center-align">Opções</th>
          </tr>

        </thead>

        <tbody>

          <tr v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">

            <td>{{ sobrevivente.id }}</td>
            <td><a @click="moreInfo = sobrevivente" data-target="moreInfo" class="more-info-link modal-trigger">{{ sobrevivente.nome }}</a></td>
            <!-- <td>{{ sobrevivente.idade }}</td>
            <td>{{ sobrevivente.sexo.toUpperCase() }}</td> -->
            <!-- <td>{{ sobrevivente.latitude }}</td>
            <td>{{ sobrevivente.longitude }}</td> -->
            <td class="center-align">
                <img v-show="sobrevivente.estaInfectado" class="zombie-img" alt="sobrevivente infectado" src="../assets/zombie2.png">
                <span v-show="!sobrevivente.estaInfectado">Não</span>
            </td>
            <td class="center-align">{{ sobrevivente.countAlertInfected }}</td>

            <td >
                <div class="center-align">
                    <button :disabled="sobrevivente.estaInfectado" @click="preEdit(sobrevivente)" class="waves-effect btn-small blue darken-1"><i class="material-icons">edit_location</i></button>
                    <button @click="infected = sobrevivente" :disabled="sobrevivente.estaInfectado" data-target="modalContaminacao" class="waves-effect btn-small red darken-1 modal-trigger"><i class="material-icons">warning</i></button>
                </div>
            </td>

          </tr>

        </tbody>
      
      </table>

        <div id="modalContaminacao" class="modal">
            <div class="modal-content">
                <h4>Alerta de Contaminação!</h4>
                <p>Digite o ID do informante da contaminação de {{ infected.nome }}:</p>
                <input type="number" placeholder="Id do informante" v-model="infoId">
            </div>
            <div class="modal-footer">
                <a href="#!" class="modal-close waves-effect waves-green btn-flat">Cancelar</a>
                <a @click="alertaInfeccao()" href="#!" class="modal-close waves-effect waves-green btn-flat">Confirmar</a>
            </div>
        </div>

        <div id="moreInfo" class="modal">
            <div class="modal-content">
                <h4>{{moreInfo.nome}}</h4>
                <span><b>Idade:</b> {{moreInfo.idade}}</span><br>
                <span><b>Sexo:</b> {{ moreInfo.sexo == "m" ? "Masculino" : "Feminino"}}</span><br>
                <span><b>Latitude:</b> {{moreInfo.latitude}}</span><br>
                <span><b>Longitude:</b> {{moreInfo.longitude}}</span><br>
            </div>
            <div class="modal-footer">
                <a href="#!" class="modal-close waves-effect waves-green btn-flat">Fechar</a>
            </div>
        </div>
    </div>

</template>

<script>

    import Sobreviventes from '../services/sobreviventes';
    import Itens from '../services/itens';
    import Message from './Message.vue'
    import Loading from './Loading.vue'

    export default {

        name: "Sobreviventes",

        data() {
            return {
                sobreviventes: [],
                sobrevivente: {
                    nome: "",
                    idade: "",
                    sexo: "",
                    latitude: "",
                    longitude: "",
                    inventario: []
                },
                itens: [],
                inventario: [],
                msg: "",
                edit: false,
                add: false,
                infected: {},
                infoId: "",
                isLoading: false,
                moreInfo: {}
            }
        },

        components: {
            Message,
            Loading,
        },

        beforeCreate() {
            this.isLoading = true
        },

        mounted() {
            this.listar()
        },

        methods: {

            scrollToTop() {
                window.scrollTo(0,0);
            },

            showMessage(message) {
                this.scrollToTop()
                this.msg = message
                setTimeout(() => this.msg = "", 4000)
            },
            
            salvar() {
                this.isLoading = true
                this.itens.forEach(item => {
                    if(parseInt(item.quantidade) > 0)
                        this.inventario.push({
                            id: item.id,
                            quantidade: parseInt(item.quantidade)
                        })
                })
                this.sobrevivente.inventario = this.inventario

                Sobreviventes.salvar(this.sobrevivente).then(response => {
                    if(response.status == 201) {
                        this.showMessage("Sobrevivente adicionado!")
                        this.listar()
                        this.sobrevivente = {}
                        this.itens = []
                        this.inventario = []
                        this.add = false
                        this.listarItens()
                    } else {
                        this.showMessage(response.data.message)
                        this.isLoading = false
                    }
                }).catch(err => {
                    if (err.response.data.message)  
                        this.showMessage(err.response.data.message)
                    else{
                        this.showMessage("Erro ao salvar")
                    }
                    this.isLoading = false
                })

            },

            editar() {
                this.isLoading = true
                Sobreviventes.atualizarLocalizacao(this.sobrevivente).then(response => {
                    if(response.status == 200) {
                        this.edit = false
                        this.showMessage(`Localização de ${this.sobrevivente.nome} atualizada!`)
                        this.sobrevivente = {}
                        this.isLoading = false
                    } else {
                        this.showMessage(response.data.message)
                        this.isLoading = false
                    }
                }).catch(err => {
                    this.showMessage("Erro ao atualizar")
                    this.isLoading = false
                })
            },

            saveOrEdit() {
                if(this.edit) {
                    this.editar()
                } else {
                    this.salvar()
                }
            },

            listar() {
                this.isLoading = true
                Sobreviventes.listar().then(response => {
                    this.sobreviventes = response.data
                    this.isLoading = false
                })
            },

            listarItens() {
                this.isLoading = true
                Itens.listar().then(response => {
                    this.itens = response.data
                    this.itens.forEach(e => {
                        e.quantidade = 0
                    })
                    this.isLoading = false
                })
            },

            preEdit(sobrevivente) {
                this.showMessage("Editar localização do sobrevivente!")
                this.edit = true
                this.sobrevivente = sobrevivente
            },

            clear() {
                this.edit = false
                this.add = false
                this.sobrevivente = {}
            },

            alertaInfeccao() {
                
                if(this.infoId != "") {
                    Sobreviventes.alertInfected(this.infoId, this.infected.id).then(response => {
                        if(response.status == 200) {
                            this.showMessage(response.data.message)
                            this.listar()
                            this.infoId = ""
                            this.infected = {}
                        }
                    }).catch(err => {
                        if (err.response.data.message)  
                            this.showMessage(err.response.data.message)
                        else
                            this.showMessage("Erro ao sinalizar contaminação!")
                    })

                } else {
                    this.showMessage("Digite um valor válido!")
                }
                
            },

            showForm() {
                this.add = true;
                this.itens = []
                this.listarItens()
            }

        }

    }

</script>

<style>

    .zombie-img {
        width: 2rem;
    }

    .save-button {
        margin: 30px 0 20px 0;
    }

    .td-input {
        width: 50px;
    }

    #moreInfo {
        top: 30% !important;
    }

    @media screen and (min-width: 800px) {
        #moreInfo {
            max-width: 20%;
        }
    }

    .more-info-link {
        cursor: pointer;
    }

</style>