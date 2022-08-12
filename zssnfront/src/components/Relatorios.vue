<template>

    <div class="container">
        
        <h4 class="center-align subtitle-page"><i class="material-icons">report</i> Relatórios da ZSSN</h4>

        <label><b>Total de Sobreviventes</b></label>
        <input type="text" disabled="true" v-model="relatorios.total_sobreviventes" >
        
        <label><b>Total de Infectados</b></label>
        <input type="text" disabled="true" v-model="relatorios.infectados" >

        <label><b>Total de Não Infectados</b></label>
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

                    this.relatorios.infectados = this.relatorios.infectados.substring(0,5) + "%"

                    
                    this.relatorios.nao_infectados = this.relatorios.nao_infectados.substring(0,5) + "%"

                    this.relatorios.media_itens.forEach(e => {
                        e.media = e.media.substring(0,5) + " por sobrevivente"
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