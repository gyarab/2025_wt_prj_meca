<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const game = ref(null)
const loading = ref(true)
const error = ref(null)

async function load() {
    try {
        loading.value = true
        const url = new URL(`/api/games/${route.params.id}`, window.location.origin)
        const res = await fetch(url)
        if (!res.ok) throw new Error(`HTTP returned ${res.status}`)
        game.value = await res.json()
    } catch (e) {
        error.value = e.message
    } finally {
        loading.value = false
    }
}

onMounted(load)
</script>

<template>
    <div class="container my-4">
        <h2 class="mb-4 text-primary border-bottom pb-2">Game Detail</h2>

        <div v-if="loading" class="d-flex justify-content-center my-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        </div>

        <div v-else-if="error" class="alert alert-danger" role="alert">
            <i class="bi bi-exclamation-triangle-fill me-2"></i>
            Failed to load game data: {{ error }}
        </div>

        <div v-else-if="game" class="card shadow-sm">
            <div class="card-header bg-dark text-white">
                <h3 class="card-title h5 mb-0">{{ game.title }}</h3>
            </div>

            <div class="card-body">
                <div class="row align-items-center text-center my-3">
                    <div class="col-5">
                        <div class="p-3 bg-light rounded border fw-bold text-truncate">
                            <span class="text-muted d-block small text-uppercase">Players: </span>
                               <strong>{{ game.white_player }}</strong> - <strong>{{ game.black_player }}</strong>
                           
                        </div>
                    </div>
                </div>

                <div class="row g-3">
                    <div class="col-md-6">
                        <div class="p-3 bg-light rounded">
                            <span class="text-muted d-block small text-uppercase">Result: </span>
                            <span class="badge bg-success fs-6 mt-1"><strong>{{ game.result }}</strong></span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="p-3 bg-light rounded">
                            <span class="text-muted d-block small text-uppercase">Moves: </span>
                            <span class="fs-5 fw-semibold mt-1 d-inline-block"><strong>{{ game.moves }}</strong></span>
                        </div>
                    </div>
                </div>
            </div>

            <hr class="text-muted" />

            <div class="card-footer bg-transparent text-end">
                <router-link to="/" class="btn btn-outline-secondary btn-sm">
                    Back to List
                </router-link>
            </div>
        </div>
    </div>
</template>