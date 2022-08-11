<template>

    <div class="container">

      <h4 class="center-align">Gerenciamento de Itens</h4>

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

  export default {
    name: 'Itens',

    data() {
      return {
        item: {
          nome: '',
          pontos: ''
        },
        itens: [],
        errors: []
      }
    },

    mounted() {
      this.listar()
    },

    methods: {
      
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
            alert("Item adicionado!")
          }
          
        }).catch(err => { 
          alert("Erro ao salvar")
          this.errors = err.response.data
        })
      },

      deletar(item) {

        if(confirm("Deseja deletar o item?")) {
          Itens.deletar(item).then(response => {
            if(response.status == 200) {
                this.listar()
                alert("Item deletado!")
            }            
            
          }).catch(err => {
            alert("Erro ao deletar")
          })
        }
        
      }

    },
}
</script>

<style>

</style>
