<script lang="ts">
    import '../app.css';
    import { Toast, toastStore } from '@brainandbones/skeleton';
    import SideBar from "$src/lib/components/sideBar.svelte";
    // import "../app.css";
</script>

<div class="text-white bg-slate-900 dark relative w-full h-screen overflow-hidden md:flex">
    <Toast background="bg-accent" width="w-12"  />
    <div class="">
        <SideBar />
    </div>
    <div class="flex-1 h-screen overflow-y-auto w-full">
     <slot/>
    </div>
</div>


