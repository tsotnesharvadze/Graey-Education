<template>
  <div>
    <h3>აირჩიეთ ბრენდი</h3>
    <ul>
      <li v-for="brand in brandList" :key="brand.id">
        <input
          type="checkbox"
          v-model="brand.value"
          @click="removeElement(brand)"
        />
        <span>{{ brand.name }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ["brandList"],
  methods: {
    removeElement(brand) {
      const ret_list = this.brandList.filter(el => el.id !== brand.id);
      this.$emit('Update:brandList', ret_list);
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 5px 10px;
}

li {
  padding: 2px 5px;
  list-style: none;
}

li input {
  margin: 2px 5px 2px 0;
}
</style>