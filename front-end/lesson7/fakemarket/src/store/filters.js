import urls from "../api/urls";
import axios from "axios";

export default {
    state() {
        return {
            categories: [],
        }
    },
    mutations: {
        updateCategories(state, newValue) {
            state.categories = newValue
        }
    },
    actions: {
        fetchCategories({ commit }) {
            axios
                .get(urls.categories)
                .then((response) => {
                    commit('updateCategories', response.data)
                });
        }
    },
    getters: {
        categories(state) {
            const retList = ['all']
            state.categories.forEach(el => retList.push(el))
            return retList
        }
    }
}