const Counter = {
    data: function () {
        return {
            counter: 2,
            counter1: 3,
            textIsShow: false,
            buttonText: 'show',
            dict: {
                a: 4,
                b: 3
            },
        }
    },
    methods: {
        mysubmit(e){
          console.log(e, 'eeee')
        },
        myClick(event){
            // event.preventDefault();
            console.log(event )
        },
        myover(event){
            const xy = [
                ['140px', '200px'],
                ['100px', '230px'],
                ['200px', '200px'],
                ['100px', '230px'],
                ['300px', '200px'],
                ['100px', '500px'],
                ['200px', '500px'],
            ];
            const old_choose = [event.target.style.top, event.target.style.left];
            let choose = xy[Math.floor(Math.random() * xy.length)];
            console.log(JSON.stringify(this.dict), JSON.parse(JSON.stringify(choose)));
            while (JSON.stringify(choose) === JSON.stringify(old_choose)){
                console.log(old_choose, choose);
                choose = xy[Math.floor(Math.random() * xy.length)];
            }
            event.target.style.top = choose[0];
            event.target.style.left = choose[1];
        }
    },
    // computed: {
    //     buttonText: {
    //         get: function () {
    //             return this.textIsShow ? 'hide' : 'show'
    //         },
    //         set: function (val) {
    //             this.textIsShow = val === 'hide';
    //         }
    //     }
    // },
    mounted: function () {
        // setTimeout(() => {
        //     console.log('gaeshva 2 wamshi')
        // }, 2000)
        //
        //
        // const aaa = function () {
        //     console.log('gaeshva 2 yovel wamshi')
        //
        // }
        //
        // const bb = setInterval(aaa, 2000);
        //
        // setTimeout(() => {
        //     clearInterval(bb)
        //
        // }, 10000)
        this.dict.a = 5

    },
    watch: {
        textIsShow: function (new_val, old_value) {
            // if (new_val){
            //     this.buttonText = 'show'
            // }else{
            //     this.buttonText = 'hide'
            // }
            this.buttonText = new_val ? 'hide': 'show'
            console.log(new_val, 'asdasdsadsa', old_value)
        },
        dict: {
            handle: function (new_val, old_val) {
                for (let k of new_val){
                    if (new_val[k] !== old_val[k])
                        console.log(k)
                }
            },
            deep : true
        }
        // buttonText: function (new_val) {
        // }
    },
    updated() {
        console.log('update')
    }

};

Vue.createApp(Counter).mount('#counter');

