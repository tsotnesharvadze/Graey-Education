<template>
  <div>
    <h1>Users Detail</h1>
    <h2>Welcome: {{ user }}</h2>
  </div>
</template>

<script>
export default {
  props: ["userId"],
  data() {
    return {
      userList: [
        { name: "giorgi", id: "914" },
        { name: "misho", id: "201" },
        { name: "cotne", id: "101" },
      ],
    };
  },
  computed: {
    user() {
      if (this.userId) {
        const new_user = this.userList.find((el) => el.id === this.userId);
        if (new_user) {
          return new_user.name;
        }
      }
      return "";
    },
  },
  mounted() {
    if (this.userList.find((el) => el.id === this.userId) === undefined) {
      this.$router.push('/404');
    }
  },
  //   mounted() {
  //     this.userId = this.$route.params.userId;
  //   },
  //   watch: {
  //     $route(route) {
  //       this.userId = route.params.userId;
  //     },
  //   },
};
</script>  