<template>

    <div class="container">
        
        <h4 class="center-align"><i class="material-icons">report</i> Relatórios da ZSSN</h4>

        <form>

            <label><b>Total de Sobreviventes</b></label>
            <input type="text" disabled="true" v-model="relatorios.total_sobreviventes" >
            
            <label>Total de Infectados</label>
            <input type="text" disabled="true" v-model="relatorios.infectados" >

            <label>Total de Não Infectados</label>
            <input type="text" disabled="true" v-model="relatorios.nao_infectados" ><br><br>

            <label><b>Média de recursos por Sobrevivente:</b></label>
            <div v-for="item in relatorios.media_itens" :key="item.index">
                <label>{{ item.item }}</label>
                <input type="text" disabled="true" :value="item.media" >
            </div><br>

            <label><b>Pontos perdidos por Sobrevivente infectado:</b></label>
            <div v-for="sobrevivente in relatorios.pontos_perdidos" :key="sobrevivente.index">
                <label>{{ sobrevivente.nome }}</label>
                <input type="text" disabled="true" :value="sobrevivente.pontos_perdidos" >
            </div> 
        
      </form>

    </div>

</template>

<script>

    import Sobreviventes from '../services/sobreviventes'

    export default {
        name: "Relatorios",
        
        data() {
            return {
                relatorios: {}
            }
        },

        mounted() {
            this.getRelatorios()
        },

        methods: {

            getRelatorios() {
                Sobreviventes.getRelatorios().then(response => {
                    this.relatorios = response.data

                    this.relatorios.media_itens.forEach(e => {
                        e.media = e.media + " por sobrevivente"
                    });

                    this.relatorios.pontos_perdidos.forEach(e => {
                        e.pontos_perdidos = e.pontos_perdidos + " pontos"
                    });

                }).catch(err => {
                    console.log(err)
                })
            }

        }
    }

</script>

<style>

label, input {
    font-size: 18px;
}

</style>