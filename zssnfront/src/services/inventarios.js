import { http } from "./Http";

export default {

    listar:() => {
        return http.get('inventarios')
    },
}