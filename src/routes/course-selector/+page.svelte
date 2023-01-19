<script lang="ts">
	import GroupTable from '$lib/components/general/GroupTable.svelte';
    import SearchInput from "$lib/components/general/SearchInput.svelte";
    import MediaQuery from "$lib/helper/MediaQuery.svelte";
    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Spinner from "$components/general/Spinner.svelte";
    import Accordion from '$lib/components/general/Accordion.svelte';
    
    import { Step } from "$types/enums";
    import { onMount } from "svelte";
   
    let data: any;
    onMount(async () => {
        await initFetch();
    });
    async function initFetch(){
        let res = await fetch("/api/course-selector/lfu?step=" + 0 + "&id=" + 0);
        res = await res.json();
        data = res.data;
    }

    let selected = Step.FieldOfStudy;
    let groups:any[] = [];
    let showGroupsModal = false;
    let showDetailModal = false;

    async function nextStep(dispatchData){
        if(!dispatchData) groups = [];
        let url = "";
        switch (selected) {
            case Step.FieldOfStudy:
            case Step.Curriculum:
            case Step.Category:
            case Step.Course:
                url = "/api/course-selector/lfu?step=" + selected + "&id=" + dispatchData?.detail.id;
                break;
            case Step.CourseType:
                url = "/api/course-selector/course?id=" + dispatchData?.detail.id;
            default:
                break;
        }
        let res = await fetch(url);
        res = await res.json();
        
        if(res.success){
            console.log("success");
            if(selected == 5){
                console.log(res.groups);
                groups = res.groups;
            }
            data = res.data;
            console.log("data", data);
            if(dispatchData?.detail.name.includes("Studieneingangs")) selected++;
            selected++;
        }
    }

</script>


<section>
    {#await initFetch()}
        <Spinner/>
    {:then}
        <MediaQuery query="(min-width: 470px)" let:matches>
            {#if matches}
                <div class="flex justify-center mx-auto items-center">
                    <ul class="steps break-all"> 
                        <li on:click={()=>{selected=0, nextStep(null)}} class="step cursor-pointer {selected >= 1 && "step-primary"}">Study</li>
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

        {#if selected <= 5}
            <div class="mt-8 flex justify-center min-w-fit max-w-full">
                <SearchInput on:GET={nextStep} data={data}/>
                <button class="btn btn-primary mx-2" on:click={()=>showDetailModal=true}>Detail</button>
            </div>
        {/if}

        {#if showDetailModal}
            <Modal open={showDetailModal} on:close={()=> showDetailModal = false}>
                <div class="max-w-3xl break-all">
                    <Table data={data}/>
                </div>
            </Modal>
        {/if}

        
        {#if groups.length > 0 && selected != 0}
            <div class="flex justify-center">
                <button class="btn btn-primary" on:click={()=> showGroupsModal=true}>Show Groups</button>
            </div>
            <Modal open={showGroupsModal} on:close={()=> showGroupsModal = false} closeOnBodyClick={false}>
                <div class="">
                    {#each groups as group,i}
                        <div class="flex justify-center flex-col max-w-full m-5">
                            <Accordion title={"Group: " + i}>
                                <GroupTable {group} />
                            </Accordion>
                        </div>
                    {/each}
                </div>
            </Modal>
        {/if}
    {:catch error}
    <div class="text-red-500">Error: {error.message}</div>
    {/await}
</section>
