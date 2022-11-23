<script lang="ts">
    import '../app.css';
    import { Toast, toastStore } from '@brainandbones/skeleton';
    import SideBar from "$src/lib/components/ui/sideBar.svelte";
    // import "../app.css";
</script>

<div class="flex fixed z-50">
	<SideBar />
</div>
<main class="relative ml-12 z-0 overflow-hidden">
    <slot />
</main>
<!-- <div class="text-white bg-slate-900 dark flex">
    <div>
        <slot/>
    </div>
</div> -->


