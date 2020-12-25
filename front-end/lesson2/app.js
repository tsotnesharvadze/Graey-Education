const app = Vue.createApp({
    data() {
        return {
            input_type: 'checkbox',
            brandNames: [
                {
                    value: false,
                    name: 'intell',
                    id: 1,
                },
                {
                    value: false,
                    name: 'dell',
                    id: 2,
                },
                {
                    value: false,
                    name: 'apple',
                    id: 3,
                },
                {
                    value: false,
                    name: 'hp',
                    id: 4,
                },
                {
                    value: false,
                    name: 'pentium :d',
                    id: 5,
                },
            ],
            // textInput: 'test text',
            // X: 4,
            // Y: 5,
            // Z: 6,
        }
    },
    methods: {
        removeValue(item) {
            item.value = false;
        },
        // sumXY() {
        //     console.log('method');
        //     return this.X + this.Y;
        // },
    },
    computed: {
        selected_filters() {
            // console.log('computed');
            function filterList(el) {
                return el.value
            };
            return this.brandNames.filter(filterList);
            // return this.brandNames.filter(el => { return el.value });
        }
    },
});

app.mount('#app');