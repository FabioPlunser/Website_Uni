<script lang="ts">
    import MediaQuery from "$helper/MediaQuery.svelte";
    export let selected: number;
    export let gotToStep: (step: number) => void;

    let steps = [
        {name: "Study", id: 0},
        {name: "Curriculum", id: 1},
        {name: "Category", id: 2},
        {name: "Course", id: 3},
        {name: "Course Type", id: 4},
        {name: "Group", id: 5},
    ]
</script>

<div>
    <MediaQuery query="(min-width: 470px)" let:matches>
        {#if matches}
            <div class="flex justify-center mx-auto items-center">
                <ul class="steps break-all"> 
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
        {:else}
            <div>
                <div class="flex justify-center">
                    <ul class="steps break-all"> 
                        {#each steps.slice(0, 3) as step, i}
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
                <div class="flex justify-center">
                    <ul class="steps break-all"> 
                        {#each steps.slice(3) as step, i}
                            {#if i < selected}
                                <!-- svelte-ignore a11y-click-events-have-key-events -->
                                <li data-content="✓" on:click={()=>{gotToStep(i)}} class="step cursor-pointer {selected >= i && "step-primary"}">{step.name}</li>
                            {:else if i == selected}
                                {#if i === 0}
                                    <li  class="step {selected >= i && "step-primary"}" style="counter-set: step 3;">{step.name}</li>
                                {:else}
                                    <li  class="step {selected >= i && "step-primary"}">{step.name}</li>
                                {/if}

                            {:else}
                                <li class="step">{step.name}</li>
                            {/if}
                        {/each}
                    </ul>  
                </div>
            </div>
        {/if}
    </MediaQuery>
</div>