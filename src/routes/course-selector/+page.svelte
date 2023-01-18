<script lang="ts">

    import type {PageData} from "./$types";

	import GroupTable from '$lib/components/general/GroupTable.svelte';
    import SearchInput from "$lib/components/general/SearchInput.svelte";
    import Accordion from "$lib/components/general/Accordion.svelte";
    import MediaQuery from "$lib/helper/MediaQuery.svelte";
    import { Step } from "$types/enums";
    
    export let data: PageData;


    $: inputData = data.data;


    let selected = Step.FieldOfStudy;
    let groups:any[] = [];


    async function nextStep(data){
        // fetch data from server to no expose RUST API
        let res = await fetch("/api/lfu?step=" + selected + "&id=" + data.detail.id);
        res = await res.json();

        if(res.success){
            if(selected == 5){
                console.log(res.groups);
                groups = res.groups;
            }
            inputData = res.data;
            selected++;

        }
    }

</script>

<section>
    <!-- <button on:click={()=>{invalidateAll()}} class="btn btn-primary mx-2">Reset</button> -->
    <MediaQuery query="(min-width: 470px)" let:matches>
        {#if matches}
            <div class="flex justify-center mx-auto items-center">
                <ul class="steps break-all"> 
                    <li on:click={()=>{selected=0, nextStep(null)}} class="step {selected >= 1 && "step-primary"}">Study</li>
                    <li class="step {selected >= 2 && "step-primary"}">Curriculum</li>
                    <li class="step {selected >= 3 && "step-primary"}">Category</li>
                    <li class="step {selected >= 4 && "step-primary"}">Course</li>
                    <li class="step {selected >= 5 && "step-primary"}">Course Type</li>
                    <li class="step {selected >= 6 && "step-primary"}">Group</li>
                </ul>  
            </div>
        {:else}
            <div>
                <div class="flex justify-center">
                    <ul class="steps break-all"> 
                        <li on:click={()=>{selected=0, nextStep(null)}} class="step {selected >= 1 && "step-primary"}">Study</li>
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

    {#if selected <= 5}
        <div class="mt-8 flex justify-center min-w-full">
            <SearchInput on:GET={nextStep} data={inputData}/>
            <!-- <button on:click={nextStep} class="btn btn-primary mx-2">Next</button> -->
        </div>
    {/if}
    
    {#if groups.length > 0 && selected != 0}
    <div class="mt-20">
        {#each groups as group}
            <div class="flex justify-center flex-col max-w-full">
                <Accordion title="Group: {group.number}">
                    <GroupTable {group} />
                </Accordion>
                
            </div>
        {/each}
    </div>
    {/if}
</section>
