<template>
  <div class="productDetailButton">
    <slot>
      <router-link :to="{ name: 'productListing' }">Home</router-link>
    </slot>
  </div>
</template>

<script>
export default {
    mounted() {
        this.$slots
    }
};
</script>

<style scoped>
.productDetailButton {
  margin: 0 auto;
  padding: 5px;
  max-width: 200px;
}
</style>

<style>
.productDetailButton > a, .productDetailButton > span{
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