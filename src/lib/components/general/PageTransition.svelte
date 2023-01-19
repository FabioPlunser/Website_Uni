<!-- PageTransition.svelte -->
<script lang="ts">
    import { fly } from "svelte/transition";
    export let url:any = null;
    const pageTransitionDuration = 500;
</script>
  
{#key url}
  <div in:fly={{y:-50, duration: 500}} >
    <slot />
  </div>
{/key}