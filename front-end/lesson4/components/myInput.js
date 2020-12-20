const myInput =  {
    template:`
        <div>
            Generate Random Number: <button @click="makeEmit">{{value}}</button>
        </div>
    `,
    props: ['value'],
    methods:{
        makeEmit(){
            console.log('asdasdasd')
            this.$emit('input',  Math.random())
        }
    }
};
