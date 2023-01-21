<script>
  import { fade, fly } from 'svelte/transition'
  import { flip } from 'svelte/animate'
  import { toast } from '$stores/toastStore'
  import ToastItem from '$components/general/ToastItem.svelte'
  
  export let options = {}
  export let target = 'default'
  
  $: toast._init(target, options)
  
  let items
  $: items = $toast.filter((i) => i.target === target)
</script>
  
<div class="fixed z-50 mt-20">
  <ul class="toast toast-top toast-end">
    {#each items as item (item.id)}
      <li
        class={item.classes.join(' ')}
        in:fly={item.intro}
        out:fade
        animate:flip={{ duration: 200 }}
      >
        <ToastItem {item} />
      </li>
    {/each}
  </ul>
</div>
  
