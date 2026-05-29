<script setup>
    import { RouterLink, RouterView} from 'vue-router'
</script>   

<template>
    <header>
        <RouterLink to="/">
        <h1> ChessDatabase (vue) </h1>
        </RouterLink>
    </header>
        <main>
        <RouterView />
        </main>
</template>