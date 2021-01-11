<template>
    <div class="filtersContainer">
        <div class="categoryFilter">
            <ul>
                <li>
                    <input :id="category+index" type="radio" name="category" v-model="selectedCategory" :value="null"
                           @change="filterByCategory">
                    <label :for="category+index">all</label>
                </li>
                <li v-for="(category, index) in categories" :key="index">
                    <input :id="category+index" type="radio" name="category" v-model="selectedCategory"
                           :value="category" @change="filterByCategory">
                    <label :for="category+index">{{category}}</label>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import urls from "../../api/urls";

    export default {
        name: "filters",
        data() {
            return {
                categories: [],
                selectedCategory: this.$route.query.category || null
            }
        },
        mounted() {
            axios.get(
                urls.categories
            ).then((response) => {
                this.categories = response.data
            });
            // this.selectedCategory = this.$route.query.category || null
        },
        methods: {
            filterByCategory() {
                this.$emit('changeCategory', this.selectedCategory)
            }
        }
    }
</script>

<style scoped>
    .filtersContainer {
        flex: 20%;
    }

    ul {
        width: 100%;
        border: 1px solid #ead2d1;
        border-radius: 6px;
    }

    li {
        padding: 5px 10px;
        /*background: #a09821;*/
        font-family: cursive;
    }

    li label {
        margin-left: 5px;
    }
</style>