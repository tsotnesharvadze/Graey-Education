import { createStore } from 'vuex';
import urls from "../api/urls";
import axios from "axios";
import productDetail from "./productDetail";

const store = createStore({
    modules: {
        det: productDetail
    },
    state() {
        return {
            productsList: [],
        }
    },
    mutations: {
        changeProductList(state, newList) {
            state.productsList = newList
        },
    },
    actions: {
        fetchNewProductList({ commit }, category) {
            const productListUrl = category
                ? urls.filterByCategory(category)
                : urls.productListing;
            axios
                .get(productListUrl)
                .then((response) => {
                    commit('changeProductList', response.data);
                });
        },
    },
    getters: {
        getProductsList(state) {
            return state.productsList
        },
    },
});

export default store;