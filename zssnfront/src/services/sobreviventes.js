import { http } from "./config";

export default {

    listar:() => {
        return http.get('sobreviventes/')
    },

    salvar:(sobrevivente) => {
        return http.post('sobrevivente/create/', sobrevivente)
    },

    atualizarLocalizacao:(sobrevivente) => {
        return http.put('sobreviventes/update/' + sobrevivente.id + 'localization', sobrevivente)
    },

    getRelatorios:() => {
        return http.get('sobreviventes/relatorios/')
    }

}