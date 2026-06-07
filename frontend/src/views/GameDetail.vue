<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const game = ref(null)

async function load() {
    const url = new URL(`/api/game/${route.params.id}`, window.location.origin)
    const res = await fetch(url)
    if (!res.ok) throw new Error(`HTTP returned ${res.status}`)
    game.value = await res.json()
}

onMounted(load)
</script>

<template>
    <h2>Game Detail</h2>
    <div v-if="game">
        <h3>{{ game.title }}</h3>
        <p>{{ game.developer.name }} ({{ game.developer.founded_year }})</p>
        <img :src="game.poster_url" style="max-height: 100px">
    </div>
</template>