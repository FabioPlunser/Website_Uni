<script lang="ts">
    import { createEventDispatcher, tick } from 'svelte';
    const dispatch = createEventDispatcher();
    import { slide, fly } from 'svelte/transition'
    import Spinner from './Spinner.svelte';

    export let data: any = null;
    
    let search = "";
    let open = false;

    function handleClick(item: any) {
        search = item.name; 
        open = false 
        dispatch('GET', item);
        search = "";
    }

    function handleKeydown({ keyCode }:any) {
        if (keyCode !== 38 && keyCode !== 40) return

        const current = document.activeElement
        const items =  [...  document.getElementsByClassName("item")]


        const currentIndex = items.indexOf(current)
        let newIndex
    
        if (currentIndex === -1) {
                newIndex = 0 
        } else {
                if (keyCode === 38) newIndex = (currentIndex + items.length - 1) % items.length
                else newIndex = (currentIndex + 1) % items.length
        }
    
        current.blur()
        items[newIndex].focus()
    }

    // $: console.log("searchInput", data);
</script>

<svelte:window on:keydown={handleKeydown} />


<div class="h-auto w-fit" on:mouseleave={()=> open = false}>
    <input on:click={()=>open=true}  type="text" placeholder="search" bind:value={search} class="w-fit input bg-base-300 " />
    {#if open}
        <div class="absolute z-[999]">
            <ul transition:slide={{duration: 200}} class="h-auto max-h-64 max-w-md bg-base-300 rounded-xl shadow-2xl mt-3 overflow-y-scroll overflow-x-scroll ">
                {#if !data}
                    <div class="p-4">
                        <Spinner size={"8"}/>
                    </div>
                {:else}
                    {#each data as item}
                        {#if item.name.toLowerCase().includes(search.toLowerCase()) }
                            <!-- svelte-ignore a11y-click-events-have-key-events -->
                            <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                            <li tabindex="0" transition:slide|local={{duration: 200}} on:keydown={(e)=>{if(e.key === "Enter") handleClick(item)}} on:click={()=> {handleClick(item)}} class="item px-5 py-1 w-full h-auto hover:bg-gray-400 cursor-pointer rounded-lg break-all focus:bg-gray-400">
                            {item.name.split("(")[0]}
                        {/if}
                    {/each}
                {/if}
            </ul>
        </div>
    {/if}
</div>

<style>
    .item:focus{
        border: 1px solid #000000;
    }
</style>