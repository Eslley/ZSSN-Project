<template>

    <div class="container">

      <h4 class="center-align">Gerenciamento de Itens</h4>

      <Message :msg="msg" v-show="msg" />

      <form @submit.prevent="salvar">

          <label>Nome</label>
          <input type="text" placeholder="Nome" v-model="item.nome" >
          
          <label>Pontos</label>
          <input type="number" placeholder="Pontos" v-model="item.pontos" >

          <button class="waves-effect waves-light btn-small blue">Salvar<i class="material-icons left">save</i></button>

      </form>

      <table class="center">

        <thead>

          <tr>
            <th>Item</th>
            <th>Pontos</th>
            <th class="center-align">Opções</th>
          </tr>

        </thead>

        <tbody>

          <tr v-for="item in itens" :key="item.id">

            <td>{{ item.nome }}</td>
            <td>{{ item.pontos }}</td>
            <td >
                <div class="center-align">
                    <button @click="deletar(item)" class="waves-effect btn-small red darken-1"><i class="material-icons">delete_sweep</i></button>
                </div>
            </td>

          </tr>

        </tbody>
      
      </table>

    </div>

</template>


<script>

  import Itens from '../services/itens';
  import Message from './Message.vue';

  export default {
    name: 'Itens',

    data() {
      return {
        item: {
          nome: '',
          pontos: ''
        },
        itens: [],
        errors: [],
        msg: ""
      }
    },

    components: {
      Message
    },

    mounted() {
      this.listar()
    },

    methods: {

      showMessage(message) {
        this.msg = message
        setTimeout(() => this.msg = "", 3000)
      },
      
      listar() {
        Itens.listar().then(response => {
          this.itens = response.data;
        })
      },

      salvar() {
        Itens.salvar(this.item).then(response => {

          if(response.status == 201) {
            this.listar()
            this.item = {}
            this.showMessage("Item adicionado!")
          }
          
        }).catch(err => { 
          this.showMessage("Erro ao salvar")
          this.errors = err.response.data
        })
      },

      deletar(item) {

        if(confirm("Deseja deletar o item?")) {
          Itens.deletar(item).then(response => {
            if(response.status == 200) {
                this.listar()
                this.showMessage("Item deletado!")
            }            
            
          }).catch(err => {
            this.showMessage("Erro ao deletar")
          })
        }
        
      }

    },
}
</script>

<style>

</style>
