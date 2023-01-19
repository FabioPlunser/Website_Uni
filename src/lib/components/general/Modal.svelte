
<script lang="ts">
	import { scale } from 'svelte/transition';
    import { createEventDispatcher, onDestroy } from 'svelte';
    const dispatch = createEventDispatcher();
	const close = () => dispatch('close');
   
    export let open = false;
    export let closeOnBodyClick = true;
    

    function handleDispatch() {

    }
    const previously_focused = typeof document !== 'undefined' && document.activeElement;
	if (previously_focused) {
		onDestroy(() => {
			previously_focused.focus();
            handleDispatch();
		});
	}
    function handleKeyDown(event) {
        if (event.key === 'Escape') {
            close();
        }
    }
</script>

<svelte:window on:keydown={handleKeyDown}/>

{#if closeOnBodyClick}
<div class="modal min-w-fit cursor-pointer max-w-none" class:modal-open={open} on:keydown={handleKeyDown} on:click={close} >
    <div transition:scale={{duration:150}} class="modal-box w-auto relative overflow-auto bg-base-300 dark:bg-slate-900 max-w-none">
            <slot/>
    </div>
</div>
{:else}
<div class="modal min-w-fit cursor-pointer max-w-none" class:modal-open={open} on:keydown={handleKeyDown} on:click|self={close} >
    <div transition:scale={{duration:150}} class="modal-box w-auto relative overflow-auto bg-base-300 dark:bg-slate-900 max-w-none">
            <slot/>
    </div>
</div>
{/if}