import { http } from "./Http";

export default {

    trocar:(trocas) => {
        return http.post('comercio/', trocas)
    },
}