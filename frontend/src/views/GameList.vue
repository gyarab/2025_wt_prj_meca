<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const games = ref([])
const router = useRouter()

async function load() {
    const url = new URL('/api/game', window.location.origin)
    const res = await fetch(url)
    if (!res.ok) throw new Error(`HTTP returned ${res.status}`)
    const data = await res.json()
    games.value = data.results

}

function selectGame(game) {
    router.push(`/game/${game.id}`)
}

onMounted(load)
</script>

<template>
    <h2>Game List</h2>

    <div v-for="game in games" @click="selectGame(game)" style="cursor: pointer;">
        <h3>{{ game.title }}</h3>
        <p>{{ game.developer.name }}</p>
        <img :src="game.poster_url" style="max-height: 100px">
    </div>

</template>