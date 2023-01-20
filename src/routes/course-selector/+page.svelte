<script lang="ts">
	import GroupTable from '$lib/components/general/GroupTable.svelte';
    import SearchInput from "$lib/components/general/SearchInput.svelte";

    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Spinner from "$components/general/Spinner.svelte";
    import Accordion from '$lib/components/general/Accordion.svelte';
    import Steps from './components/Steps.svelte';
    import { Step } from "$types/enums";
    import { onMount } from "svelte";
    import { selectorSteps } from '$stores/selectorSteps';
   
    let _selectorSteps = $selectorSteps;
    let data: any;
    let selected = Step.FieldOfStudy;
    let groups:any[] = [];
    let showGroupsModal = false;
    let showDetailModal = false;

    $: 

    onMount(async () => {
        await initFetch();
    });
    async function initFetch(){
        let res = await fetch("/api/course-selector/lfu?step=" + Step.FieldOfStudy + "&id=" + 0);
        res = await res.json();
        if(res.success){
            data = res.data;
        }
    }

   

    async function nextStep(dispatchData: any){
        if(!dispatchData) groups = [];
        console.log("nextStep: selected: " + selected + " dispatchData: ");
        console.log(dispatchData.detail);
        selected++;
        let res = null;
        res = await fetch("/api/course-selector/lfu?step=" + selected + "&id=" + dispatchData.detail.id);

        
        if(res){
            res = await res.json();
            console.log("nextStep", res);
            if(res.success) {
                data = res.data;
                if(dispatchData?.detail.name.includes("Introduction")) selected+2;
                $selectorSteps[selected].id = dispatchData?.detail.id;
            }
        }
    }

    async function gotToStep(step: number){
        let res = await fetch("/api/course-selector/lfu?step=" + step + "&id=" + _selectorSteps[step]?.id || "0");
        res = await res.json();
        console.log("gotToStep", res);
        if(res?.success){
            data = res.data;
            selected = step;
        }
    }

</script>


<section>
    {#if !data}
        <Spinner/>
    {:else}
        <Steps bind:selected {gotToStep}/>

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
    {/if}
</section>
