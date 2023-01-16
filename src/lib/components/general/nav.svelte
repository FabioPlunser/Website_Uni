<script lang="ts">
  import favicon  from '$assets/favicon.svg';
  import { navButtonsStore } from "$stores/navButtonsStore";

  $: buttons = $navButtonsStore;
</script>

<div class="flex p-2 justify-center bg-slate-900 w-full rounded-none justiy-center shadow-2xl top-0 fixed z-10">
  <div class="flex justify-between">
    <div class="fixed left-0 flex items-center mx-1">
      <a href="/" class=""><img src={favicon} alt="logo" class="w-12 rounded-full shadow-xl"/></a>
    </div>

    <div class="flex justify-center items-center">
      {#each buttons as button}
        {#if button?.href}
          <a class="flex justify-center btn btn-primary mx-2" href={button.href}>{@html button.text}</a>
        {:else}
          <button class="flex justify-center btn btn-primary mx-2" on:click={button.action}>{@html button.text}</button>
        {/if}
      {/each}
    </div>
  </div>
</div>