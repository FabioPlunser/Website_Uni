<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();
    import { slide, fly } from 'svelte/transition'

    export let data: any = null;
    
    let search = "";
    let open = false;

    function handleClick(item: any) {
        search = item.name; 
        open = false 
        dispatch('GET', item);
        search = "";
    }

    // $: console.log("searchInput", data);
</script>


<div class="w-full h-auto max-w-xl" on:mouseleave={()=>open=false}>
    <input on:click={()=>open=true}  type="text" placeholder="search" bind:value={search} class="input w-full bg-base-300 " />
    {#if open}
        <ul transition:slide={{duration: 200}} class="w-full h-auto max-h-48 bg-base-300 rounded-xl shadow-xl mt-1 overflow-y-scroll">
            {#each data as item}
                {#if item.name.toLowerCase().includes(search.toLowerCase()) }
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <li transition:slide|local={{duration: 200}} on:click={()=> {handleClick(item)}} class="px-5 py-1 w-full h-auto hover:bg-gray-400 cursor-pointer rounded-lg break-all">
                        <span>{item.name}</span>
                    </li>
                {/if}
            {/each}
        </ul>
    {/if}
</div>