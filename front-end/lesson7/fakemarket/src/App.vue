<template>
  <router-view></router-view>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "App",
  methods: {
      ...mapActions(['fetchCategories'])
  },
  mounted() {
      this.fetchCategories();
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  /*box-sizing: border-box;*/
}

#app {
  padding: 10px;
  display: flex;
}
</style>
