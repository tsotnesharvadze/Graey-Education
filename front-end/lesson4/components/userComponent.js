const userComponent = {
    template: `
    <div>
        <a href="#" @mouseover="sendDetailRequest" @mouseleave="leaveShakoMouse">{{user.username}}</a>
        <div v-if="isShow">
            <p>{{detailData.username}}</p>
            <p>{{detailData.name}}</p>
            <p>{{detailData.email}}</p>
            <p>{{detailData.phone}}</p>
            <p>company:{{detailData.company.name}}</p>
            <a :href="'http://' + detailData.website" v-text="detailData.website"></a>
        </div>
    </div>
       
    `,
    props: ['user', 'value'],
    data() {
        return {
            detailData: {},
            isShow: false
        }
    },
    methods: {
        sendDetailRequest() {
            this.$emit('mouseIsOver', this.user.username);
            this.$emit('input', this.user.username);
            if (!Object.keys(this.detailData).length){
                axios.get(
                    `https://jsonplaceholder.typicode.com/users/${this.user.id}`,
                )
                .then((response) => {
                    this.detailData = response.data;
                    this.isShow = true;
                })
                .catch(function (error) {
                    console.log(error);
                })
            }else{
                this.isShow = true;
            }
        },
        leaveShakoMouse(){
            this.isShow = false;
        }
    }
};
