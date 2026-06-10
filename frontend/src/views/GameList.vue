<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const games = ref([])
const router = useRouter()

async function load() {
    try {
        const url = new URL('/api/games', window.location.origin)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`HTTP returned ${res.status}`)
        const data = await res.json()
        games.value = data.results
    } catch (error) {
        console.error("Chyba při načítání her:", error)
    }
}

function selectGame(game) {
    router.push(`/game/${game.id}`)
}

onMounted(load)
</script>

<template>
    <div class="container my-4">

        <h2 class="mb-4 text-primary border-bottom pb-2">Game List</h2>

        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">

            <div v-for="game in games" :key="game.id" class="col">

                <div @click="selectGame(game)" class="card h-100 shadow-sm border-0 bg-light clickable-card">
                    <div class="card-body d-flex flex-column justify-content-between">

                        <div>
                            <h5 class="card-title text-dark fw-bold mb-3">
                                {{ game.title || 'Game without title' }} 
                            </h5>

                            <p class="card-text mb-2">
                                <span class="badge bg-secondary text-wrap p-2 w-100 text-start">
                                    ⚪ White: <strong class="float-end">{{ game.white_player }}</strong>
                                </span>
                            </p>
                            <p class="card-text mb-3">
                                <span class="badge bg-dark text-wrap p-2 w-100 text-start">
                                    ⚫ Black: <strong class="float-end">{{ game.black_player }}</strong>
                                </span>
                            </p>
                        </div>

                        <div
                            class="border-top pt-2 mt-2 d-flex justify-content-between align-items-center text-muted small">
                            <span>Moves: <strong>{{ game.moves }}</strong></span> <br>
                            <span class="badge bg-success px-2 py-1 mx-2"> Result: <strong>{{ game.result }}</strong></span>
                        </div>

                    </div>
                </div>

            </div>

        </div>
    </div>
</template>

<style scoped>
/* Drobný CSS trik pro lepší vizuální odezvu při najetí myší */
.clickable-card {
    cursor: pointer;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.clickable-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}
</style>