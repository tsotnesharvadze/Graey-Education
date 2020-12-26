<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in userList" :key="user.id">
        <router-link :to="{ name: 'userDetail', params: { userId: user.id } }">
          {{ user.name }}</router-link
        >
      </li>
    </ul>
    <router-view :userId="$route.params.userId"></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userList: [
        { name: "giorgi", id: 914 },
        { name: "misho", id: 201 },
        { name: "cotne", id: 101 },
      ],
    };
  },
};
</script>  