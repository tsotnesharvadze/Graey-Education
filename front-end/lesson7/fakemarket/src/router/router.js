import {createRouter, createWebHistory} from "vue-router";
import ProductListing from "../components/ProductListing";
import ProductDetail from "../components/ProductDetail";
import description from "../components/productComponents/description";
import images from "../components/productComponents/images";

const routes = [
    {
        path: '/', component: ProductListing, name: 'productListing', meta: {
            isSecure: true
        }
    },
    {
        path: '/detail/:id', component: ProductDetail, name: 'productDetail', children: [
            {
                path: '', component: description, name: 'productDescription',
                meta: {
                    linkTitle: 'See Images',
                    linkName: 'productImages'
                }
            },
            {
                path: 'images', component: images, name: 'productImages', meta: {
                    linkTitle: 'See Description',
                    linkName: 'productDescription'
                }
            }
        ]
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router