<script lang="ts">
    import {slide} from "svelte/transition"
    let open=false;
    export let title = "";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div transition:slide={{duration:400}} on:click={()=> open=!open} class="collapse w-full overflow-y-auto max-w-full collapse-arrow border border-base-100 bg-base-300 rounded-box cursor-pointer">
    <div class="collapse-title text-2xl font-bold">
        {title}
    </div>
    
    {#if open}
    <div class="m-10" transition:slide={{duration:400}}>
        <slot/>
    </div>
    {/if}
</div>