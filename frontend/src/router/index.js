import { createRouter, createWebHistory } from "vue-router";
import GameList from "../views/GameList.vue";
import GameDetail from "../views/GameDetail.vue";

const router = createRouter({
    history: createWebHistory(),
    routes : [
        { path: '/', name: 'home', component : GameList },
        { path: '/games/:id', name: 'game-detail', component : GameDetail }
    ]
});

export default router;