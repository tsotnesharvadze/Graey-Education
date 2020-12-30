<template>
<div style="width: 1020px">
        <carousel :items-to-show="4" :wrap-around="true" :transition="300">
        <slide v-for="product in products" :key="product.id">
            <product-card :product="product"></product-card>
        </slide>
        <template #addons>
            <navigation/>
            <pagination/>
        </template>
    </carousel>
</div>
</template>

<script>
    import {Carousel, Navigation, Pagination, Slide} from 'vue3-carousel';
    import ProductCard from "../UI/ProductCard";
    import 'vue3-carousel/dist/carousel.css';

    export default {
        name: "images",
        props: ['product'],
        components: {
            Carousel,
            Slide,
            ProductCard,
            Pagination,
            Navigation
        },

        computed: {
            products() {
                const products = [];
                for (let i = 0; i < 10; i++) {
                    products.push(this.product)
                }
                return products
            }
        }

    }
</script>

<style scoped>

</style>