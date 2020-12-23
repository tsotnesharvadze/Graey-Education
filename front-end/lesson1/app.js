Vue.createApp({
    data() {
        return {
            inputValue: '',
            valueList: [],
        }
    },
    methods: {
        addValue() {
            if (this.inputValue !== '') {
                this.valueList.push(this.inputValue);
                this.inputValue = '';
            }
        }
    },
}).mount('#app');


// const buttonEl = document.querySelector('button');
// const inputEl = document.querySelector('input');
// const listEl = document.querySelector('ul');

// function addValue() {
//     const value = inputEl.value;
//     const listItem = document.createElement('li');
//     listItem.textContent = value;
//     listEl.appendChild(listItem);
//     inputEl.value = '';
// }

// buttonEl.addEventListener('click', addValue);