<script lang="ts">
    export let stepCount: number;
    export let gotToStep: (step: number) => void;

    let steps = [
        {name: "Study", id: 0},
        {name: "Curriculum", id: 1},
        {name: "Category", id: 2},
        {name: "Course", id: 3},
    ]
</script>


<div class="flex justify-center items-center w-full">
    <ul class="steps break-all w-full"> 
        {#each steps as step, i}
            {#if i < stepCount}
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <li data-content="✓" on:click={()=>{gotToStep(i)}} class="step cursor-pointer {stepCount >= i && "step-primary"}">{step.name}</li>
            {:else if i == stepCount}
                <li  class="step {stepCount >= i && "step-primary"}">{step.name}</li>
            {:else}
                <li class="step">{step.name}</li>
            {/if}
        {/each}
    </ul>  
</div>
        