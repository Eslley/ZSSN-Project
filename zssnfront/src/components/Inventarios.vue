<template>

  <div class="container">
      
    <h4 class="center-align subtitle-page"><i class="material-icons">domain</i> Inventários</h4>

    <Loading :isLoading="isLoading"/>

    <table class="center">

      <thead>

        <tr>
          <th>Sobrevivente</th>
          <th class="center-align">Inventário</th>
        </tr>

      </thead>

      <tbody>

        <tr v-for="inventario in inventarios" :key="inventario.sobreviventeId">

          <td>{{ inventario.sobrevivente }}</td>

          <td class="center-align">
            <div class="collection">
              <a href="#!" v-for="item in inventario.itens" :key="item.index" class="collection-item">
                {{ item.item.nome }}: <span class="badge">{{ item.quantidade }}</span>
              </a>
            </div>
          </td>

        </tr>

      </tbody>
    
    </table>

  </div>
</template>

<script>

    import Inventarios from '../services/inventarios'
    import Loading from './Loading.vue'

    export default {
        name: "Inventarios",

        data() {
          return {
              inventarios: [],
              isLoading: false
          }
        },

        components: {
          Loading
        },

        mounted() {
          this.getInventarios()
        },

        methods: {
          getInventarios() {
            this.isLoading = true
              Inventarios.listar().then(response => {
                  this.inventarios = response.data.inventarios
                  this.isLoading = false
              }).catch(err => {
                this.isLoading = false
              })
          }
        }
    }

</script>

<style scoped>

  .collection {
    border: none;
  }

</style>