<script lang="ts">
    import '../app.css';
    import Nav from "$lib/components/general/Nav.svelte";
    import PageTransition from '$lib/components/general/PageTransition.svelte';
    import SvelteToast from '$components/general/SvelteToast.svelte';
    import Footer from '$lib/components/general/Footer.svelte';

    import { page } from "$app/stores"
</script>

<Nav/>
<SvelteToast/>
<div class="divider m-0"/> 

<PageTransition url={$page.url.pathname}>
    <main class="m-10 min-h-screen">
        <slot />
    </main>
</PageTransition>


<Footer/>