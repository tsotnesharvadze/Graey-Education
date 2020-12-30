<template>
    <div class="container">
        <div v-for="product in productsList" :key="product.id" class="productContainer">
            <div class="productTitle">
                <p>{{product.title}}</p>
            </div>
            <div class="productImageContainer">
                <img :src="product.image" alt="">
            </div>
            <div class="productDetailButton">
                <router-link :to="{name: 'productDetail', params:{id: product.id}}">
                    See Detail
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../api/urls";

    export default {
        name: "productListing",
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
    .productContainer{
        width: 300px;
        height: 480px;
        border: 1px solid #c384845e;
        padding: 10px;
        text-align: center;
    }
    .productTitle{
        padding: 10px;
        border-bottom: 1px solid gray;
        height: 40px;
        font-family: cursive;

    }
    .productImageContainer{
        width: 300px;
        height: 340px;
        margin: 20px auto 0 auto;

    }
    .productImageContainer img{
        width: 100%;
        height: 100%;
        object-fit: contain;
    }
    .productDetailButton{
        margin: 0 auto;
        padding: 5px;
    }
    .productDetailButton > a{
        display: block;
        height: 30px;
        margin: 0 auto;
        color: white;
        background: black;
        text-decoration: none;
        padding: 10px;
        line-height: 30px;
    }

</style>