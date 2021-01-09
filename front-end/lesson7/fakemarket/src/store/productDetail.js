import urls from "../api/urls";
import axios from "axios";

export default {
    namespaced: true,
    state() {
        return {
            relatedProducts: [],
            productDetal: {
                id: 0,
                title: '',
                price: '',
                category: '',
                description: '',
                image: ''
            }
        }
    },
    mutations: {
        setProductDetail(state, newDetail) {
            state.productDetal = newDetail
        },
        setRelatedProductList(state, newList) {
            state.relatedProducts = newList
        },
    },
    actions: {
        fetchRelatedProducts({ commit, state, getters }) {
            axios
                .get(urls.productListing)
                .then((response) => {
                    commit('setRelatedProductList', response.data)
                });
        },
        fetchProductDetailById({ commit }, productId) {
            axios
                .get(urls.productDetail(productId))
                .then((response) => {
                    commit('setProductDetail', response.data)
                })
        }
    },
    getters: {
        productDetal(state) {
            return state.productDetal
        },
        relatedProducts(state) {
            return state.relatedProducts
        }
    },
}