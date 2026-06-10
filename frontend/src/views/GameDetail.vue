<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const game = ref(null)

async function load() {
    const url = new URL(`/api/games/${route.params.id}`, window.location.origin)
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
        <p>Players: {{ game.white_player }} - {{ game.black_player }}</p>
        <p>Moves: {{ game.moves }}</p>
        <p>Result: {{ game.result }}</p>
    </div>
</template>