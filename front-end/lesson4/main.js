Vue.createApp({
    components:{
        userComponent,
        myInput
    },
    data(){
        return {
            data: [],
            selectedUser: '',
            myText: 'click me'
        }
    },
    methods:{
      // changeSelectedUserName(username){
      //     this.selectedUser = username
      // }
        aaa(a){
            console.log(a, 's')
        }
    },
    mounted(){
        axios.get(
            'https://jsonplaceholder.typicode.com/users/',
            )
          .then((response) => {
              this.data = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })

    }
}).mount('#app');
