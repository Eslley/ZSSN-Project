<template>

  <div class="container">
      
      <h4 class="center-align subtitle-page"><i class="material-icons">domain</i> Inventários</h4>

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

    export default {
        name: "Inventarios",

        data() {
          return {
              inventarios: []
          }
        },

        mounted() {
          this.getInventarios()
        },

        methods: {
          getInventarios() {
              Inventarios.listar().then(response => {
                  this.inventarios = response.data.inventarios
              }).catch(err => {

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