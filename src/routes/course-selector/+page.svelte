<script lang="ts">
    import type {PageData} from "./$types";

	import GroupTable from '$lib/components/general/GroupTable.svelte';
    import SearchInput from "$lib/components/general/SearchInput.svelte";
  import Accordion from "$lib/components/general/Accordion.svelte";


    enum Step {
        new,
        FieldOfStudy,
        Curriculum,
        Category,
        Course,
        CourseType,
        Group
    }
    export let data: PageData;
    $: inputData = data.data;
    let selected = Step.FieldOfStudy;
    let groups:any[] = [];
    async function nextStep(data){
        let url = "";
        switch (selected) {
            case 0: 
                url = "http://localhost:3001/lfu";
                break;
            case 1: 
            case 2:
            case 3:
            case 4:
                url = `http://localhost:3001/lfu/${data.detail.id}`;
                break;
            case 5: 
                url = `http://localhost:3001/course/${data.detail.id}`;
                break;
            default:
                break;
        }

        let res = await fetch(url);
        res = await res.json();
        console.log("selected: " + selected);
        console.log(res);
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
    <div class="flex justify-center mx-auto items-center">
        <!-- {#if selected < 4} -->
            <ul class="steps break-all"> 
                <li on:click={()=>{selected=0, nextStep(null)}} class="step {selected >= 1 && "step-primary"}">Study</li>
                <li class="step {selected >= 2 && "step-primary"}">Curriculum</li>
                <li class="step {selected >= 3 && "step-primary"}">Category</li>
                <li class="step {selected >= 4 && "step-primary"}">Course</li>
                <li class="step {selected >= 5 && "step-primary"}">Course Type</li>
                <li class="step {selected >= 6 && "step-primary"}">Group</li>
            </ul>  
        <!-- {/if} -->
    </div>
    {#if selected <= 5}
        <div class="mt-8 flex justify-center min-w-full">
            <SearchInput on:GET={nextStep} data={inputData}/>
            <!-- <button on:click={nextStep} class="btn btn-primary mx-2">Next</button> -->
        </div>
    {/if}
    {#if groups.length > 0}
        {#each groups as group}
            <div class="flex justify-center flex-col max-w-full">
                <Accordion title="Group: {group.number}">
                    <GroupTable {group} />
                </Accordion>
                
            </div>
        {/each}
    {/if}
</section>
