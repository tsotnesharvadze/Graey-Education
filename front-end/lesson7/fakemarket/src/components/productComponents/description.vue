<template>
    <div class="productTitle">
    <h1>{{product.title}}</h1>
    </div>
    <div class="productDescription">
        {{product.description}}
    </div>
</template>

<script>
    export default {
        name: "description",
        props: ['product']
    }
</script>

<style scoped>

</style>