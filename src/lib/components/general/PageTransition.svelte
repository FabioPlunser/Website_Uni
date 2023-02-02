<!-- PageTransition.svelte -->
<script lang="ts">
    import { fly } from "svelte/transition";
    export let url:any = null;
</script>
  
{#key url}
  {#if url.includes("files")}
      <slot />
  {:else}
    <div in:fly={{y: -50, duration: 300}} >
      <slot />
    </div>
  {/if}
{/key}