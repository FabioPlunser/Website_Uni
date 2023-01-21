<script lang="ts">

    
    import SearchInput from "$components/general/SearchInput.svelte";
    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Steps from './components/Steps.svelte';
    import Calendar from './components/Calendar.svelte';

    import { Step } from "$types/enums";
    import { onMount } from "svelte";
    import { selectorSteps } from '$stores/selectorSteps';
    import { convertToDate } from "$helper/convertTime";
  import GroupTable from "./components/GroupTable.svelte";
   
    let _selectorSteps = $selectorSteps;
    let data: any;
    let selected = Step.FieldOfStudy;
    let groups:any[] = [];
    let showGroupModal = false;
    let showDetailModal = false;
    let selectedGroup:any = null;


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
        selected++;
        if(dispatchData?.detail.name.includes("Studies Induction")) selected++;
        let res = null;
        data = null;
        res = await fetch("/api/course-selector/lfu?step=" + selected + "&id=" + dispatchData.detail.id);

        
        if(res){
            res = await res.json();
            if(res.success) {
                console.log("nextStep", res);
                if(res?.groups){
                    groups = res.groups;
                    return;
                }
                data = res.data;
                $selectorSteps[selected].id = dispatchData?.detail.id;
            }
        }
    }

    async function gotToStep(step: number){
        let res = await fetch("/api/course-selector/lfu?step=" + step + "&id=" + _selectorSteps[step]?.id || "0");
        res = await res.json();
        // console.log("gotToStep", res);
        if(res?.success){
            data = res.data;
            selected = step;
        }
    }

    $:{
        for (let group of groups){
            let times = [];
            for(let time of group.times){
                let {from, to} = convertToDate(time);
                times.push({
                    from: from,
                    to: to,
                    time: time.time,
                    location: time.location,
                    comment: time.comment
                });
            }
            group.times = times;
        }

        groups = [...groups];
    }
</script>


<section>
    <Steps bind:selected {gotToStep}/>

    {#if selected <= 5 && groups.length==0}
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

    <br class="mt-12"/>
    {#if groups.length > 0 && selected != 0}
        <div class="grid grid-cols-4 gap-2">
            {#each groups as group, i}
                <div class="card w-auto bg-primary max-w-xs -rotate-2">
                    <div class="card w-auto bg-base-300 shadow-xl max-w-xs rotate-2">
                        <div class="card-body items-center text-center">
                            <h2 class="card-title">{`Group: ${group.number}`}</h2>
                            <div class="flex">
                                <p class="mx-2">{group?.times[0]?.from.toLocaleString("de-De", {weekday: 'short'})} : {group?.times[0]?.from.toLocaleString("de-De", {day: 'numeric', month: 'numeric', year: 'numeric'})}</p>
                                <p class="mx-2">{group?.times[0]?.from.toLocaleString('de-De', { hour: '2-digit', minute: '2-digit'})} - {group?.times[0]?.to?.toLocaleString('de-De', { hour: '2-digit', minute: '2-digit'})}</p>
                            </div>
                            <p>Location: {group.times[0].location}</p>
                            <p>Comment: {group.times[0].comment}</p>
                            <div class="card-actions justify-between">
                                <button class="btn btn-success" on:click={()=>{selectedGroup=group}}>Select</button>
                                <button class="btn btn-secondary" on:click={()=>{selectedGroup=group, showGroupModal=true}}>Details</button>
                              </div>
                        </div>

                    </div>
                </div>
            {/each}
        </div>
    {:else if selected > 4 && groups.length == 0}
        <div class="flex justify-center">
            <h1 class="text-4xl">No Groups found</h1>
        </div>
    {/if}

    {#if showGroupModal}
        <Modal open={showGroupModal} on:close={()=> showGroupModal = false}>
            <div class="max-w-3xl break-all">
                <GroupTable group={selectedGroup}/>
            </div>
        </Modal>
    {/if}

    {#if selected > 4}
        <div class="flex justify-center">
            <Calendar/>
        </div>
    {/if}

</section>
