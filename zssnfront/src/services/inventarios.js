import { http } from "./Http";

export default {

    listar:() => {
        return http.get('inventarios')
    },

    getInventario:(sobreviventeId) => {
        return http.get(`inventarios/sobrevivente/${sobreviventeId}/`)
    }
}