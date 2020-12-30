<template>
    <div class="productDetailContainer" v-if="product.id">
        <div class="productDetailHeader">
           <span><router-link :to="{name: 'productListing'}">Home</router-link></span> ➨ <span>{{product.category}}</span> ➨ <span>{{product.title}}</span>
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
                <div class="productTitle">
                    <h1>{{product.title}}</h1>
                </div>
                <div class="productDescription">
                    {{product.description}}
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../api/urls";

    export default {
        name: "ProductDetail",
        data() {
            return {
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
            axios.get(
                urls.productDetail(this.$route.params.id)
            ).then((response) => {
                this.product = response.data
            })
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

</style>