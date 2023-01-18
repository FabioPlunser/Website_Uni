<script let="ts">
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    import { slide } from 'svelte/transition'

    export let data = null;
    
    let search = "";
    let open = false;
    let selected = false;

    function handleClick(item) {
        search = item.name; 
        open = false 
        selected = true;
        dispatch('GET', item.id);
    }

    
</script>


<div class="w-auto h-auto">
    <input on:click={()=>open=true} type="text" placeholder="search" bind:value={search} class="mt-20 input min-w-full bg-base-300 " />
    {#if open}
        <ul transition:slide={{duration: 200}} class="w-full h-auto max-h-48 bg-base-300 rounded-xl shadow-xl mt-2 overflow-y-hidden">
            {#each data as item}
                {#if item.name.toLowerCase().includes(search.toLowerCase()) }
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <li on:click={()=> {handleClick(item)}} class="px-5 py-1 w-full h-auto hover:bg-gray-400 cursor-pointer rounded-lg">
                        <span >{item.name}</span>
                    </li>
                {/if}
            {/each}
        </ul>
    {/if}
</div>