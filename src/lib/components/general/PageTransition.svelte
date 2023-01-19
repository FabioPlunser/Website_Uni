<!-- PageTransition.svelte -->
<script lang="ts">
    import { fly } from "svelte/transition";
    export let url:any = null;
</script>
  
{#key url}
  <div in:fly={{y: -50, duration: 300}} >
    <slot />
  </div>
{/key}