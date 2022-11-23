<script lang="ts">
    import { slide } from "svelte/transition";

    export let open = false;
    export let title = "";
</script>

<div class="relative  w-auto overflow-hidden">
    <div
        on:click={() => {
            open = !open;
        }}
        class="bg-slate-800 cursor-pointer h-12 w-full pl-5 flex items-center {open
            ? 'rounded-t-lg'
            : 'rounded-lg'}"
    >
        <h1 class="text-lg">{title}</h1>
    </div>
    <div
        class="absolute top-3 right-3 transition-transform duration-200 {open
            ? 'rotate-0'
            : 'rotate-180'}"
    >
        <i class="bi bi-caret-down" />
    </div>
    {#key open}
        <div
            transition:slide|local
            class="bg-slate-800 transition-all duration-500 pl-5 pb-5 rounded-b-lg {open
                ? 'block'
                : 'hidden'}"
        >
            <slot />
        </div>
    {/key}
</div>
