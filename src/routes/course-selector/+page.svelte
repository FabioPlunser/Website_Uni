<script lang="ts">    
    import SearchInput from "$lib/components/general/SearchDropdown.svelte";
    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Steps from './components/Steps.svelte';
    import { selectorSteps, groups } from "$stores/selectorSteps";
    import { addToast } from "$helper/addToToastStore";
    import { onMount } from "svelte";

    let showGroupModal = false;
    let showDetailModal = false;
    $: selected = $selectorSteps[$selectorSteps.length-1].currentStep;
    export let data:any = null;
    $: console.log(data);

    async function gotToStep(){

    }

    async function nextStep(){

    }
</script>


<section class="z-0">
    <div class=" justify-center w-full">
        <Steps bind:selected {gotToStep}/>
        <div class="mt-8 flex justify-center w-full">
            <SearchInput on:GET={nextStep} bind:data={data?.studies}/>
            <button class="btn btn-primary mx-2" on:click={()=>showDetailModal=true}>Detail</button>
        </div>
    </div>
   
    <br class="mt-12"/>


    {#if showDetailModal}
        <Modal open={showDetailModal} on:close={()=> showDetailModal = false}>
            <div class="max-w-3xl break-all">
                <Table data={data}/>
            </div>
        </Modal>
    {/if}


</section>
