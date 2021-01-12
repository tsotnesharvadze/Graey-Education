<template>
  <div class="productContainer">
    <div class="productTitle" v-if="$slots.title">
        <slot name="title" :title="product.title" :id="product.id"></slot>    
    </div>
    <div class="productImageContainer">
        <slot name="image"></slot>    
    </div>
    <button-default>

      <router-link :to="{ name: 'productDetail', params: { id: product.id } }">
        See Detail
      </router-link>

    </button-default>
  </div>
</template>

<script>
import DefaultButton from "./DefaultButton.vue";

export default {
  name: "ProductCard",
  props: ["product"],
  components: {
      'button-default': DefaultButton,
  }
};
</script>

<style>
.productContainer {
  width: 250px;
  height: 480px;
  border: 1px solid #c384845e;
  padding: 10px;
  text-align: center;
}
.productTitle {
  padding: 10px;
  border-bottom: 1px solid gray;
  height: 40px;
  font-family: cursive;
}
.productImageContainer {
  width: 250px;
  height: 340px;
  margin: 20px auto 0 auto;
}
.productImageContainer img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>