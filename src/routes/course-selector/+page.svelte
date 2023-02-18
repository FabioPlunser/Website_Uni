<script lang="ts">    
    import SearchInput from "$lib/components/general/SearchDropdown.svelte";
    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Steps from './components/Steps.svelte';
    import { selectorSteps, groups } from "$stores/selectorSteps";
    import { addToast } from "$helper/addToToastStore";
    import { onMount } from "svelte";

    let showDetailModal = false;
    let stepCount = 0;
    $: stepCount = $selectorSteps[$selectorSteps.length-1].currentStep;

    export let data:any = null;
    data = data?.studies;
    $: console.log(data);
    $: console.log(stepCount);
    async function gotToStep(){

    }

    async function nextStep(data:any){
        console.log(data?.detail);

        stepCount++;
    }
</script>


<section class="z-0">
    <div class="mx-auto justify-center w-full max-w-2xl">
        <Steps bind:stepCount {gotToStep}/>
        <div class="mt-8 flex justify-center w-full">
            <SearchInput on:GET={nextStep} bind:data/>
            <button class="btn btn-primary mx-2" on:click={()=>showDetailModal=true}>Detail</button>
        </div>
    </div>
   
    <br class="mt-12"/>


    {#if showDetailModal}
        <Modal open={showDetailModal} on:close={()=> showDetailModal = false}>
            <div class="w-full">
                <table class="table table-zebra table-compact  rounded-lg">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Description</th>
                        <th>Link</th>
                    </tr>
                    </thead>
                    <tbody>
                    {#each data as row}
                        <tr class="">
                            {#each Object.values(row) as value}
                                <td class="break-all"><p class="break-all">{value}</p></td>
                            {/each}
                            <td><a class="btn btn-primary" target="_blank" rel="noopener noreferrer" href={`https://lfuonline.uibk.ac.at/public/lfuonline_lv.home?r=${Object.values(row)[0]}`}>LFU</a></td>
                        </tr>
                    {/each}
                    
                    </tbody>
                </table>
            </div>
        </Modal>
    {/if}


</section>
