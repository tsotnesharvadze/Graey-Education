import { createStore } from 'vuex';
import urls from "../api/urls";
import axios from "axios";
import productDetail from "./productDetail";
import Filters from "./filters";

const store = createStore({
    modules: {
        det: productDetail,
        filter: Filters,
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