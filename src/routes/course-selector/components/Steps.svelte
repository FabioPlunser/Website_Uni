<script lang="ts">
    import MediaQuery from "$helper/MediaQuery.svelte";
    export let selected: number;
    export let gotToStep: (step: number) => void;

    let steps = [
        {name: "Study", id: 0},
        {name: "Curriculum", id: 1},
        {name: "Category", id: 2},
        {name: "Course", id: 3},
    ]
</script>


<div class="flex justify-center items-center">
    <ul class="steps break-all md:w-[800px]"> 
        {#each steps as step, i}
            {#if i < selected}
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <li data-content="✓" on:click={()=>{gotToStep(i)}} class="step cursor-pointer {selected >= i && "step-primary"}">{step.name}</li>
            {:else if i == selected}
                <li  class="step {selected >= i && "step-primary"}">{step.name}</li>
            {:else}
                <li class="step">{step.name}</li>
            {/if}
        {/each}
    </ul>  
</div>
        