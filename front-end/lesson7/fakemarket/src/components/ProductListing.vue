<template>
    <filters @changeCategory="changeCategory"></filters>
    <div class="container">
        <product-card v-for="product in productsList" :key="product.id" :product="product">

        </product-card>
    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../api/urls";
    import ProductCard from "./UI/ProductCard";
    import Filters from "./productListingComponents/filters";

    export default {
        name: "productListing",
        components: {
            Filters,
            ProductCard
        },
        data() {
            return {
                productsList: []
            }
        },
        mounted() {
            // console.log(this.$route.meta)
            this.fetchProductListing(this.$route.query.category)
        },
        methods: {
            fetchProductListing(category) {
                const productListUrl = category ?
                    urls.filterByCategory(category) : urls.productListing;
                axios.get(
                    productListUrl
                ).then((response) => {
                    this.productsList = response.data;
                    const query = {...this.$route.query};
                    if (category)
                        query.category = category;
                    else{
                        delete query.category
                    }
                    this.$router.replace({
                        query
                        // query: query
                    });
                })
            },
            changeCategory(category) {
                this.fetchProductListing(category)
            }
        }
    }
</script>

<style scoped>
    .container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        column-gap: 10px;
        row-gap: 20px;
        flex: 80%;
    }

</style>