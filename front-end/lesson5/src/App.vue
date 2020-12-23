<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png" />
    <list-display v-model:brandList="brandNames"></list-display>
    <p>{{brandNames}}</p>
  </div>
</template>

<script>
import Test from "./components/Test.vue";

export default {
  name: "App",
  data() {
    return {
      brandNames: [
        {
          value: false,
          name: "intell",
          id: 1,
        },
        {
          value: false,
          name: "dell",
          id: 2,
        },
        {
          value: false,
          name: "apple",
          id: 3,
        },
        {
          value: false,
          name: "hp",
          id: 4,
        },
        {
          value: false,
          name: "pentium :d",
          id: 5,
        },
      ],
    };
  },
  components: {
    "list-display": Test,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
