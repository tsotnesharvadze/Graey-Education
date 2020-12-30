import {createRouter, createWebHistory} from "vue-router";
import ProductListing from "../components/ProductListing";
import ProductDetail from "../components/ProductDetail";

const routes = [
    {
        path: '/', component: ProductListing, name: 'productListing', meta: {
            isSecure: true
        }
    },
    {path: '/detail/:id', component: ProductDetail, name: 'productDetail'}
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router