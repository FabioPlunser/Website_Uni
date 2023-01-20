<script lang="ts">
    import MediaQuery from "$helper/MediaQuery.svelte";
    export let selected = 0;
    export let nextStep: any = null;
</script>


<MediaQuery query="(min-width: 470px)" let:matches>
    {#if matches}
        <div class="flex justify-center mx-auto items-center">
            <ul class="steps break-all"> 
                {#if selected > 1}
                    <li data-content="✓" on:click={()=>{selected=0, nextStep(null)}} class="step cursor-pointer {selected >= 1 && "step-primary"}">Study</li>
                {:else}
                    <li class="step cursor-pointer {selected >= 1 && "step-primary"}">Study</li>
                {/if}
                {#if selected > 2}
                    <li data-content="✓" class="step {selected >= 2 && "step-primary"}">Curriculum</li>
                {:else}
                    <li class="step {selected >= 2 && "step-primary"}">Curriculum</li>
                {/if}
                {#if selected > 3}
                    <li data-content="✓" class="step {selected >= 3 && "step-primary"}">Category</li>
                {:else}
                    <li class="step {selected >= 3 && "step-primary"}">Category</li>
                {/if}
                {#if selected > 4}
                    <li data-content="✓" class="step {selected >= 4 && "step-primary"}">Course</li>
                {:else}
                    <li class="step {selected >= 4 && "step-primary"}">Course</li>
                {/if}
                {#if selected > 5}
                    <li data-content="✓" class="step {selected >= 5 && "step-primary"}">Course Type</li>
                {:else}
                    <li class="step {selected >= 5 && "step-primary"}">Course Type</li>
                {/if}
                {#if selected > 6}
                    <li data-content="✓" class="step {selected >= 6 && "step-primary"}">Group</li>
                {:else}
                    <li class="step {selected >= 6 && "step-primary"}">Group</li>
                {/if}
            </ul>  
        </div>
    {:else}
        <div>
            <div class="flex justify-center">
                <ul class="steps break-all"> 
                    <li on:click={()=>{selected=0, nextStep(null)}} class="step cursor-pointer {selected >= 1 && "step-primary"}">Study</li>
                    <li class="step {selected >= 2 && "step-primary"}">Curriculum</li>
                    <li class="step {selected >= 3 && "step-primary"}">Category</li>
                </ul>  
            </div>
            <div class="flex justify-center">
                <ul class="steps break-all"> 
                    <li class="step {selected >= 4 && "step-primary"}" style="counter-set: step 3;">Course</li>
                    <li class="step {selected >= 5 && "step-primary"}">Course Type</li>
                    <li class="step {selected >= 6 && "step-primary"}">Group</li>
                </ul>  
            </div>
        </div>
    {/if}
</MediaQuery>