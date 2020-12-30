<template>
    <div class="productDetailContainer" v-if="product.id">
        <div class="productDetailHeader">
            <span><router-link :to="{name: 'productListing'}">Home</router-link></span> ➨
            <span>{{product.category}}</span> ➨ <span>{{product.title}}</span>
        </div>
        <div class="productContentContainer">
            <div class="productDetailLeftSide">
                <div class="productGallery">
                    <img :src="product.image" alt="">
                </div>
                <div class="productPrice">
                    <p>Price: <strong>{{product.price}}</strong></p>
                </div>
            </div>
            <div class="productDetailRightSide">
                <router-link :to="{name: $route.meta.linkName}">{{$route.meta.linkTitle}}</router-link>
                <router-view :product="product"></router-view>
            </div>
        </div>
        <div class="relatedProductsCarousel" v-if="relatedProducts.length">
            <carousel :items-to-show="4" :wrap-around="true" :transition="300">
                <slide v-for="product in relatedProducts" :key="product.id">
                    <product-card :product="product"></product-card>
                </slide>
                <template #addons>
                    <navigation/>
                    <pagination/>
                </template>
            </carousel>
        </div>

    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../api/urls";
    import {Carousel, Navigation, Pagination, Slide} from 'vue3-carousel';
    import ProductCard from "./UI/ProductCard";
    import 'vue3-carousel/dist/carousel.css';

    export default {
        name: "ProductDetail",
        components: {
            Carousel,
            Slide,
            ProductCard,
            Pagination,
            Navigation
        },
        data() {
            return {
                relatedProducts: [],
                product: {
                    id: 0,
                    title: '',
                    price: '',
                    category: '',
                    description: '',
                    image: ''
                }
            }
        },
        mounted() {
            this.fetchData()
        },
        methods: {
            fetchData() {
                axios.get(
                    urls.productListing
                ).then((response) => {
                    this.relatedProducts = response.data
                });
                axios.get(
                    urls.productDetail(this.$route.params.id)
                ).then((response) => {
                    this.product = response.data
                })
            },

        },
        watch: {
            $route() {
                this.fetchData();
                window.scrollTo({top: 0, behavior: 'smooth'});
            }
        }
    }
</script>

<style scoped>
    .productDetailHeader {
        padding: 20px;
        font-size: 24px;
        font-family: cursive;
        color: #dcb541;
    }

    .productContentContainer {
        display: flex;
        justify-content: space-around;
    }

    .productGallery img {
        width: 400px;
        height: auto;
    }

    .relatedProductsCarousel {
        margin: 0 auto;
        width: 90%;
    }

</style>