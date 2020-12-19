Vue.createApp({
    data(){
        return {
            data: [],
            userDetail: {}
        }
    },
    methods:{
      sendDetailRequest(userId) {
          axios.get(    //
            `https://jsonplaceholder.typicode.com/users/${userId}`,
            )
          .then((response) => {
              this.userDetail = response.data;
          })
          .catch(function (error) {
            console.log(error);
          })
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
