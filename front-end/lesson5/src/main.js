import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router';

import UserList from './pages/UserList.vue'
import TeamList from './pages/TeamList.vue'
import userDetail from './components/UserDetail.vue'
import PageNotFound from './pages/404.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/users' },
        {
            path: '/users', component: UserList, name: 'userList', children: [
                { path: '/users/:userId', component: userDetail, name: 'userDetail', props: true },
            ]
        }, // www.sdas.ge/users
        { path: '/groups', component: TeamList, name: 'teamsListing' },
        { path: '/:notFount(.*)', component: PageNotFound, name: '404' },
    ],
    // linkActiveClass: 'active',
    // linkExactActiveClass: 'exact'
})

const app = createApp(App)

app.use(router)

app.mount('#app')