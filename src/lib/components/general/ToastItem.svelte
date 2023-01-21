<script>
  import { onMount, onDestroy } from 'svelte'
  import { tweened } from 'svelte/motion'
  import { linear } from 'svelte/easing'
  import { toast } from '$stores/toastStore'
  
  export let item
  
  const progress = tweened(item.initial, { duration: item.duration, easing: linear })
  const close = () => toast.pop(item.id)
  const autoclose = () => {
    if ($progress === 1 || $progress === 0) {
      close()
    }
  }
  let next = item.initial
  let prev = next
  let paused = false
  
  $: if (next !== item.next) {
    next = item.next
    prev = $progress
    paused = false
    progress.set(next).then(autoclose)
  }
  
  const pause = () => {
    if (!paused && $progress !== next) {
      progress.set($progress, { duration: 0 })
      paused = true
    }
  }
  
  const resume = () => {
    if (paused) {
      const d = item.duration
      const duration = d - d * (($progress - prev) / (next - prev))
      progress.set(next, { duration }).then(autoclose)
      paused = false
    }
  }
  
  let componentProps = {}
  $: if (item.component) {
    const { props = {}, sendIdTo } = item.component
    componentProps = { ...props, ...(sendIdTo && { [sendIdTo]: item.id }) }
  }
  
  const check = (prop, kind = 'undefined') => typeof prop === kind
  // `progress` has been renamed to `next`; shim included for backward compatibility, to remove in next major
  $: if (!check(item.progress)) {
    item.next = item.progress
  }
  
  let unlisten
  const listen = (d = document) => {
    if (check(d.hidden)) return
    const handler = () => (d.hidden ? pause() : resume())
    const name = 'visibilitychange'
    d.addEventListener(name, handler)
    unlisten = () => d.removeEventListener(name, handler)
    handler()
  }
  
  onMount(listen)
  onDestroy(() => {
    if (check(item.onpop, 'function')) {
      item.onpop(item.id)
    }
    unlisten && unlisten()
  })

  function handleKeydown(e){
    if (e instanceof KeyboardEvent && ['Enter', ' '].includes(e.key)) close()
  }
</script>
  
<div class="alert {item.theme.toString().length>0 ? `${item.theme.toString()}` : "alert-info"}">
  <div class="">
    {#if item.component}
      <svelte:component this={item.component.src} {...componentProps} />
    {:else}
      {@html item.msg}
    {/if}
  </div>
  {#if item.dismissable}
  <button class="btn btn-sm" on:click={close} on:keydown={handleKeydown}> 
    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
  </button>
  {/if}
</div>
