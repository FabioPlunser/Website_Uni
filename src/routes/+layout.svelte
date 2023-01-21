<script lang="ts">
    import '../app.css';
    import Nav from "$lib/components/general/Nav.svelte";
    import PageTransition from '$lib/components/general/PageTransition.svelte';
    import { page } from "$app/stores"
    import SvelteToast from '$components/general/SvelteToast.svelte';
    
</script>

<Nav/>
<SvelteToast/>
<div class="divider m-0"/> 
<PageTransition url={$page.url.pathname}>
    <main class="m-10">
        <slot />
    </main>
</PageTransition>
