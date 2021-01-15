<template>
  <div>
    <filters>
      <template v-slot:categoryName="propsData">

        <button-default>
          
          <span
            :class="{ 'active': selectedCategory === propsData.displayTitle }"

            @click="fetchProductListing(propsData.displayTitle)"

            >{{ propsData.displayTitle }}</span
          >
        </button-default>
      </template>
    </filters>
    <div class="container">
      <product-card
        v-for="product in productsList"
        :key="product.id"
        :product="product"
      >
        <template #title="propsList">
          <p>{{ propsList.title }} - {{ propsList.id }}</p>
        </template>
        <template #image>
          <img :src="product.image" alt="" />
        </template>
      </product-card>
    </div>
  </div>
</template>

<script>
import ProductCard from "./UI/ProductCard";
import Filters from "./productListingComponents/filters";
import { mapGetters, mapActions } from "vuex";
import DefaultButton from "./UI/DefaultButton.vue";

export default {
  name: "productListing",
  data() {
    return {
      selectedCategory: this.$route.query.category || "all",
    };
  },
  components: {
    Filters,
    ProductCard,
    "button-default": DefaultButton,
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
    ...mapActions(["fetchNewProductList"]),
    fetchProductListing(category) {
      this.selectedCategory = category
      if (category === "all") {
        category = "";
      }
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

span.active {
  color: red;
}
</style>