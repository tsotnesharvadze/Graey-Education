<template>
  <div>
    <h1>Header</h1>
    <router-link :to="{name: 'teamsListing'}">Teams link</router-link>
    <router-link to="/users">Users link</router-link>
    <router-link :to="{name:'userDetail', params: {userId: 914}}">Users Detail</router-link>
  </div>
</template>

<script>
export default {};
</script>  

