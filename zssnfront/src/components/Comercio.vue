<template>

    <div class="container">
      
      <h4 class="center-align subtitle-page"><i class="material-icons">swap_horiz</i> Comércio</h4>

      <Message :msg="msg" v-show="msg"/>

      <Loading :isLoading="isLoading"/>

      <div class="row two-inputs">
        
        <div class="col m6 s12">
          <input class="center-align" placeholder="Id do 1° sobrevivente" type="number" v-model="id1">
        </div>

        <div class="col m6 s12">
          <input class="center-align" placeholder="Id do 2° sobrevivente" type="number" v-model="id2" >
        </div>
      </div>

      <div class="center-align search-button">
            <button @click="buscar()" class="waves-effect waves-light btn-small">Buscar Sobreviventes<i class="material-icons left">search</i></button>
      </div>

      <div class="row">

        <div v-if="sobrevivente1.itens != undefined" class="col l6 m12 s12">
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">Sobrevivente: {{ sobrevivente1.sobrevivente }}</span>
              
              <span>Inventário</span>
              <ul class="collection">
                <li v-for="(item, index) in sobrevivente1.itens" :key="item.index" class="collection-item">
                  <div> <span class="item-name">{{ item.item.nome }}: {{item.quantidade}}x</span> 
                    <a @click="addItem1(item, index)" href="#!" class="secondary-content">
                      <i class="material-icons">arrow_forward</i>
                      <span>Ofertar 1</span>
                    </a>
                  </div>
                </li>
              </ul>
              
              <span>Itens Ofertados:</span>
              <ul class="collection">
                <li v-for="(item, index) in comercio.sobrevivente1.itens" :key="item.index" class="collection-item">
                  <div> 
                    <span class="item-name">{{ item.item.nome }}: {{item.quantidade}}x</span> 
                    <a @click="removeItem1(index)" href="#!" class="secondary-content">
                      <i class="material-icons">arrow_back</i>
                      <span>Retirar 1</span>
                    </a>
                  </div>
                </li>
              </ul>

              <div class="center-align total-pontos white"><span class="">Total de Pontos Ofertados: {{ totalPontos1 }}</span></div>
            </div>
          </div>
        </div>

        <div v-if="sobrevivente2.itens" class="col l6 m12 s12">
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">Sobrevivente: {{ sobrevivente2.sobrevivente }}</span>
              
              <span>Inventário</span>
              <ul class="collection">
                <li v-for="(item, index) in sobrevivente2.itens" :key="item.index" class="collection-item">
                  <div> <span class="item-name">{{ item.item.nome }}: {{item.quantidade}}x</span> 
                    <a @click="addItem2(item, index)" href="#!" class="secondary-content">
                      <i class="material-icons">arrow_forward</i>
                      <span>Ofertar 1</span>
                    </a>
                  </div>
                </li>
              </ul>

              <span>Itens Ofertados:</span>
              <ul class="collection">
                <li href="#!" v-for="(item, index) in comercio.sobrevivente2.itens" :key="item.index" class="collection-item">
                  <div> <span class="item-name">{{ item.item.nome }}: {{item.quantidade}}x</span> 
                    <a @click="removeItem2(index)" href="#!" class="secondary-content">
                      <i class="material-icons">arrow_forward</i>
                      <span>Retirar 1</span>
                    </a>
                  </div>
                </li>
              </ul>
              
              <div class="center-align total-pontos white"><span>Total de Pontos Ofertados: {{ totalPontos2 }}</span></div>
            </div>
          </div>
        </div>

      </div>

      
      <div v-if="sobrevivente1.itens != undefined && sobrevivente2.itens != undefined" class="col l2 m12 s12 center-align vertical-align">
          <button :disabled="totalPontos1 == 0 || totalPontos2 == 0 || totalPontos1 != totalPontos2" @click="requestTroca()" class=" btn-small">Trocar<i class="material-icons left">swap_horiz</i></button>
      </div>

    </div>
</template>

<script>

  import Comercio from '../services/comercio';
  import Inventarios from '../services/inventarios';
  import Message from './Message.vue'
  import Loading from './Loading.vue'

  export default {
    name: "Comercio",

    data() {
      return {
        id1: "",
        id2: "",
        totalPontos1: 0,
        totalPontos2: 0,
        sobrevivente1: {},
        sobrevivente2: {},
        msg: "",
        comercio: {
          sobrevivente1: {
            sobrevivente: "",
            itens: []
          },
          sobrevivente2: {
            sobrevivente: "",
            itens: []
          }
        },
        isLoading: false
      }
    },

    components: {
      Message,
      Loading
    },

    methods: {

      scrollToTop() {
                window.scrollTo(0,0);
      },

      showMessage(message) {
        this.scrollToTop()
        this.msg = message
        setTimeout(() => this.msg = "", 3000)
      },

      buscar() {
        this.isLoading = true

        this.sobrevivente1 = {}
        this.sobrevivente2 = {}
        this.totalPontos1 = 0
        this.totalPontos2 = 0

        if(this.id1 == this.id2 || this.id1 == "" || this.id2 == "" ){
          this.showMessage("Preencha os campos corretamente!")
          this.isLoading = false
        } else {

          Inventarios.getInventario(this.id1).then(response => {
            Inventarios.getInventario(this.id2).then(response2 => {
              if(response.status == 200 && response2.status == 200) {

                this.comercio.sobrevivente1.itens = JSON.parse(JSON.stringify(response.data.itens))              
                this.comercio.sobrevivente2.itens = JSON.parse(JSON.stringify(response2.data.itens))    
                this.zerarItensOferecidos()

                this.sobrevivente1 = response.data
                this.sobrevivente2 = response2.data

                this.isLoading = false
              }
            }).catch(err => {
              this.isLoading = false
              this.showMessage("Erro ao buscar sobrevivente!")
              if(err.response.data.message) {
                this.showMessage((err.response.data.message))
              }
            })
          }).catch(err => {
            this.isLoading = false
            this.showMessage("Erro ao buscar sobrevivente!")
            if(err.response.data.message) {
              this.showMessage((err.response.data.message))
            }
          })

        }

      },

      zerarItensOferecidos(){
        this.comercio.sobrevivente1.itens.forEach(e => {
          e.quantidade = 0
        })

        this.comercio.sobrevivente2.itens.forEach(e => {
          e.quantidade = 0
        })
      },  

      addItem1(item, index) {
        if(!item.quantidade == 0){
          this.comercio.sobrevivente1.itens[index].quantidade += 1
          item.quantidade -= 1
          this.totalPontos1 += item.item.pontos
        }
      },

      removeItem1(index) {
        if(!this.comercio.sobrevivente1.itens[index].quantidade == 0) {
          this.comercio.sobrevivente1.itens[index].quantidade -= 1
          this.sobrevivente1.itens[index].quantidade += 1
          this.totalPontos1 -= this.sobrevivente1.itens[index].item.pontos
        }
      },

      addItem2(item, index) {
        if(!item.quantidade == 0){
          this.comercio.sobrevivente2.itens[index].quantidade += 1
          item.quantidade -= 1
          this.totalPontos2 += item.item.pontos
        }
      },

      removeItem2(index) {
        if(!this.comercio.sobrevivente2.itens[index].quantidade == 0) {
          this.comercio.sobrevivente2.itens[index].quantidade -= 1
          this.sobrevivente2.itens[index].quantidade += 1
          this.totalPontos2 -= this.sobrevivente2.itens[index].item.pontos
        }
      },

      requestTroca() {
        this.isLoading = true
        if(this.totalPontos1 == this.totalPontos2) {
          this.comercio.sobrevivente1.sobrevivente = this.sobrevivente1.sobreviventeId

          this.comercio.sobrevivente2.sobrevivente = this.sobrevivente2.sobreviventeId

          this.preComercio()

          Comercio.trocar(this.comercio).then(response => {
            this.isLoading = false
            if(response.status == 200) {
              this.showMessage("Troca realizada com sucesso!")
              this.clearData()
            } else {
              this.showMessage(response.data.message)
            }
          }).catch(err => {
            if(err.response.data.message) {
              this.showMessage(err.response.data.message)
            }
          })
        } else {
          this.isLoading = false
          this.showMessage("A quantidade de pontos oferecidos é diferente!");
        }
        
      },

      preComercio() {
        this.comercio.sobrevivente1.itens.forEach(e => {
          e.id = e.item.id
          e.pontos = e.item.pontos
        })

        this.comercio.sobrevivente2.itens.forEach(e => {
          e.id = e.item.id
          e.pontos = e.item.pontos
        })

        this.comercio.sobrevivente1.itens = this.comercio.sobrevivente1.itens.filter(e => {
          return e.quantidade > 0 
        })

        this.comercio.sobrevivente2.itens = this.comercio.sobrevivente2.itens.filter(e => {
          return e.quantidade > 0 
        })
      },

      clearData() {
        this.id1 = ""
        this.id2 = ""
        this.sobrevivente1 = {}
        this.sobrevivente2 = {}
        this.totalPontos1 = 0
        this.totalPontos2 = 0
      }

    }
  }

</script>

<style scoped>
  
  .two-inputs {
    margin-bottom: 2px !important;
  }

  .search-button {
    margin: 10px 0 10px 0;
  }

  .total-pontos {
    color: black;
    padding: 0 5px 0 5px !important;
    border-radius: 5px;
  }

  .collection button {
    margin-left: 10px;
  }

  .collection-tem span {
    color: black !important;
  }

  .item-name {
    color: #26a69a;
  }

  li .secondary-content {
    display: flex;
  }
  .collection .collection-item {
    padding: 7px 7px;
  }
</style>

