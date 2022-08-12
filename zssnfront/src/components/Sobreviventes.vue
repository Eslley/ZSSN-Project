<template>
    
    <div class="container">

        <h4 class="center-align subtitle-page"><i class="material-icons">people</i> Sobreviventes</h4>

        <Message :msg="msg" v-show="msg" />

        <form action="#" @submit.prevent="">

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
                <button @click="clear()" class="waves-effect waves-light btn-small">Limpar<i class="material-icons left">clear</i></button>
                <button @click="saveOrEdit()" class="waves-effect waves-light btn-small blue">Salvar<i class="material-icons left">save</i></button>
            </div>
      </form>

      <table class="center">

        <thead>

          <tr>
            <th>Id</th>
            <th>Nome</th>
            <!-- <th>Idade</th>
            <th>Sexo</th> -->
            <th>Latitude</th>
            <th>Longitude</th>
            <th class="center-align">Infectado</th>
            <th class="center-align">Alertas</th>

            <th class="center-align">Opções</th>
          </tr>

        </thead>

        <tbody>

          <tr v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">

            <td>{{ sobrevivente.id }}</td>
            <td>{{ sobrevivente.nome }}</td>
            <!-- <td>{{ sobrevivente.idade }}</td>
            <td>{{ sobrevivente.sexo.toUpperCase() }}</td> -->
            <td>{{ sobrevivente.latitude }}</td>
            <td>{{ sobrevivente.longitude }}</td>
            <td class="center-align">
                <img v-show="sobrevivente.estaInfectado" class="zombie-img" alt="sobrevivente infectado" src="../assets/zombie2.png">
                <span v-show="!sobrevivente.estaInfectado">Não</span>
            </td>
            <td class="center-align">{{ sobrevivente.countAlertInfected }}</td>

            <td >
                <div class="center-align">
                    <button @click="preEdit(sobrevivente)" class="waves-effect btn-small blue darken-1"><i class="material-icons">edit_location</i></button>
                    <button @click="showModalAlert(sobrevivente)" class="waves-effect btn-small red darken-1"><i class="material-icons">warning</i></button>
                </div>
            </td>

          </tr>

        </tbody>
      
      </table>

    </div>

</template>

<script>

    import Sobreviventes from '../services/sobreviventes';
    import Itens from '../services/itens';
    import Message from './Message.vue'

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
                edit: false
            }
        },

        components: {
            Message
        },

        mounted() {
            this.listar()
            this.listarItens()
        },

        methods: {

            showModalAlert() {

            },

            scrollToTop() {
                window.scrollTo(0,0);
            },

            showMessage(message) {
                this.scrollToTop()
                this.msg = message
                setTimeout(() => this.msg = "", 4000)
            },
            
            salvar() {
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
                        this.listarItens()
                    } else {
                        this.showMessage(response.data.message)
                    }
                }).catch(err => {
                    if (err.response.data.message)  
                        this.showMessage(err.response.data.message)
                    else{
                        this.showMessage("Erro ao salvar")
                    }
                })

            },

            editar() {
                Sobreviventes.atualizarLocalizacao(this.sobrevivente).then(response => {
                    if(response.status == 200) {
                        this.edit = false
                        this.showMessage(`Localização de ${this.sobrevivente.nome} atualizada!`)
                        this.sobrevivente = {}
                    } else {
                        this.showMessage(response.data.message)
                    }
                }).catch(err => {
                    console.log(err)
                    this.showMessage("Erro ao atualizar")
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
                Sobreviventes.listar().then(response => {
                    this.sobreviventes = response.data
                })
            },

            listarItens() {
                Itens.listar().then(response => {
                    this.itens = response.data
                    this.itens.forEach(e => {
                        e.quantidade = 0
                    })
                })
            },

            preEdit(sobrevivente) {
                this.showMessage("Editar localização do sobrevivente!")
                this.edit = true
                this.sobrevivente = sobrevivente
            },

            clear() {
                this.edit = false
                this.sobrevivente = {}
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
</style>