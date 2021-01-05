<template>
    <div>
        <div class="container">
            <input id="search" type="text" v-model="textValue" placeholder="Search for product">
        </div>
        <div class="container">
            <product-card v-for="product in filterSearch" :key="product.id" :product="product">

            </product-card>
        </div>
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
                productsList: [],
                textValue: '',
            }
        },
        mounted(){
            // console.log(this.$route.meta)
            axios.get(
                urls.productListing
            ).then((response)=>{
                this.productsList = response.data
            })
        },
        computed:{
            filterSearch: function(){
                return this.productsList.filter((product) => {
                    return product.title.toLowerCase().match(this.textValue.toLowerCase())
                });
            }
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
    #search{
        padding: 10px;
        margin-bottom: 10px;
        width: 50%;
        
    }

</style>