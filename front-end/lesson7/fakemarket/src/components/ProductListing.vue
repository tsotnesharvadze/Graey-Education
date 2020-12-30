<template>
    <div class="container">
        <product-card v-for="product in productsList" :key="product.id" :product="product">

        </product-card>
    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../api/urls";
    import ProductCard from "./UI/ProductCard";

    export default {
        name: "productListing",
        components: {
          ProductCard
        },
        data(){
            return {
                productsList: []
            }
        },
        mounted(){
            // console.log(this.$route.meta)
            axios.get(
                urls.productListing
            ).then((response)=>{
                this.productsList = response.data
            })
        }
    }
</script>

<style scoped>
    .container{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        column-gap: 10px;
        row-gap: 20px;
    }

</style>