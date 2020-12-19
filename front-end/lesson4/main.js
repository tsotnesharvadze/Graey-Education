Vue.createApp({
    components:{
        userComponent
    },
    data(){
        return {
            data: [],
            userDetail: {}
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
