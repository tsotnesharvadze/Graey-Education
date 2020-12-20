const myInput =  {
    template:`
        <div>
            Generate Random Number: <button @click="makeEmit">{{modelValue}}</button>
        </div>
    `,
    props: ['modelValue'],
    methods:{
        makeEmit(){
            this.$emit('update:modelValue',  Math.random())
        }
    }
};
