<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper">
        <a href="#" class="brand-logo">ZSSN S1ST3M</a>
        <a href="#" data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
        <ul class="right hide-on-med-and-down">
          <li :class="{ active: page == 'sobreviventes' }"><a @click="page='sobreviventes'">Sobreviventes</a></li>
          <li :class="{ active: page == 'inventarios' }"><a @click="page='inventarios'">Inventários </a></li>
          <li :class="{ active: page == 'itens' }"><a @click="page='itens'">Itens</a></li>
          <li :class="{ active: page == 'comercio' }"><a @click="page='comercio'">Comércio</a></li>
          <li :class="{ active: page == 'relatorios' }"><a @click="page='relatorios'">Relatórios</a></li>
        </ul>

        <ul class="sidenav" id="mobile-demo">
          <li :class="{ active: page == 'sobreviventes' }"><a @click="page='sobreviventes'">Sobreviventes</a></li>
          <li :class="{ active: page == 'inventarios' }"><a @click="page='inventarios'">Inventários </a></li>
          <li :class="{ active: page == 'itens' }"><a @click="page='itens'">Itens</a></li>
          <li :class="{ active: page == 'comercio' }"><a @click="page='comercio'">Comércio</a></li>
          <li :class="{ active: page == 'relatorios' }"><a @click="page='relatorios'">Relatórios</a></li>
        </ul>
      </div>
    </nav>

    <Itens v-show="page == 'itens'" />
    <Sobreviventes v-show="page == 'sobreviventes'" />
    <Inventarios v-show="page == 'inventarios'" />

  </div>
</template>


<script>

import Itens from './components/Itens.vue'
import Sobreviventes from './components/Sobreviventes.vue'
import Inventarios from './components/Inventarios.vue'

export default {
  name: "App",

  data() {
    return {
      page: "sobreviventes",
      active: ""
    }
  },

  components: {
    Itens,
    Sobreviventes,
    Inventarios,
    Sobreviventes,
    Inventarios
  }
  
}

</script>

<style>

  nav {
    margin-bottom: 1rem;
  }

  #sidenav-overlay {
    margin-left: 300px;
  }

</style>
