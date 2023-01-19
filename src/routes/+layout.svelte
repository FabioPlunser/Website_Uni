<script lang="ts">
    import '../app.css';
    import Nav from "$lib/components/general/Nav.svelte";
    import PageTransition from '$lib/components/general/PageTransition.svelte';
    import { page } from "$app/stores"
</script>

<Nav/>
<div class="divider m-0"/>
<main class="m-10">
    <PageTransition url={$page.url}>
        <slot />
    </PageTransition>
</main>

