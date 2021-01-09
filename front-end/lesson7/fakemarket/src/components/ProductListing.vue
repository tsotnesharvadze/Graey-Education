<template>
  <div>
    <filters @changeCategory="fetchProductListing"></filters>
    <div class="container">
      <product-card
        v-for="product in productsList"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import ProductCard from "./UI/ProductCard";
import Filters from "./productListingComponents/filters";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "productListing",
  components: {
    Filters,
    ProductCard,
  },
  computed: {
    ...mapGetters({
      productsList: "getProductsList",
    }),
  },
  mounted() {
    this.fetchProductListing(this.$route.query.category);
  },
  methods: {
    ...mapActions(['fetchNewProductList']),
    fetchProductListing(category) {
      this.fetchNewProductList(category).then(() => {
        const query = { ...this.$route.query };
        if (category) query.category = category;
        else {
          delete query.category;
        }
        this.$router.replace({
          query,
        });
      });
    },
  },
};
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