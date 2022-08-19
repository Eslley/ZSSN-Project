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
          <li class="sidenav-close" :class="{ active: page == 'sobreviventes' }"><a @click="page='sobreviventes'">Sobreviventes</a></li>
          <li class="sidenav-close" :class="{ active: page == 'inventarios' }"><a @click="page='inventarios'">Inventários </a></li>
          <li class="sidenav-close" :class="{ active: page == 'itens' }"><a @click="page='itens'">Itens</a></li>
          <li class="sidenav-close" :class="{ active: page == 'comercio' }"><a @click="page='comercio'">Comércio</a></li>
          <li class="sidenav-close" :class="{ active: page == 'relatorios' }"><a @click="page='relatorios'">Relatórios</a></li>
        </ul>
      </div>
    </nav>

    <Itens v-show="page == 'itens'" />
    <Sobreviventes v-show="page == 'sobreviventes'" />
    <Inventarios v-if="page == 'inventarios'" />
    <Comercio v-if="page == 'comercio'"/>
    <Relatorios v-if="page == 'relatorios'" />

  </div>
</template>


<script>

import Itens from './components/Itens.vue'
import Sobreviventes from './components/Sobreviventes.vue'
import Inventarios from './components/Inventarios.vue'
import Relatorios from './components/Relatorios.vue'
import Comercio from './components/Comercio.vue'

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
    Inventarios,
    Relatorios,
    Comercio
}
  
}

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
    var elems1 = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems1, {});
  })

</script>

<style>

  body {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
  }
  .main {
      flex: 1 0 auto;
  }

  nav {
    margin-bottom: 1rem;
  }

  #sidenav-overlay {
    margin-left: 300px;
  }

  .nav-wrapper .right {
    margin-right: 20px;
  }

  h4 .material-icons {
    font-size: 35px;
    line-height: inherit;
  }

  .subtitle-page {
      font-size:28px;
      line-height:24px;
  }

  .subtitle-page .material-icons {
      display: inline-flex;
      vertical-align: top;
  }

  nav .brand-logo {
    font-size: 1.9rem !important;
  }

  .nav-wrapper {
    padding-left: 20px;
  }

</style>
