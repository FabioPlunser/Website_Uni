<script lang="ts">    
    import SearchInput from "$components/general/SearchInput.svelte";
    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Steps from './components/Steps.svelte';
    import GroupTable from "./components/GroupTable.svelte";
    import Spinner from "$components/general/Spinner.svelte";
    import MyCalendar from "./components/MyCalendar.svelte";
    import Calendar from "./components/Calendar.svelte";
    import { selectorSteps, groups } from "$stores/selectorSteps";
    import { addToast } from "$helper/addToToastStore";
    import { onMount } from "svelte";
    import { slide, fly} from "svelte/transition";

    let showGroupModal = false;
    let showDetailModal = false;
    let showGroups = true;
    let selectedGroup:any = null;
    $: selected = $selectorSteps[$selectorSteps.length-1].currentStep;
    let events:any[] = [];
    let data:any = null;
    
    onMount(async ()=>{
        await initFetch();
        
    })

    async function initFetch(){
        let res = await fetch(`/api/course-selector/lfu?step=${selected}&id=${$selectorSteps[selected].id}`);
        res = await res.json();
        data = res?.data;
    }

    async function nextStep(dispatchData:any){
        let _selected = selected;
        $groups = [];
        if(selected < 3){
            data = null;
            let res = await fetch(`/api/course-selector/lfu?step=${++_selected}&id=${dispatchData?.detail?.id}`);
            res = await res.json();
            // console.log(res);
            if(res?.success){
                selected++;
                data = res?.data;
                $selectorSteps[selected].id = dispatchData?.detail?.id;
                $selectorSteps[$selectorSteps.length-1].currentStep = selected;
            }else{
                addToast(res?.message, "alert-error");
            }
        }
        if(selected >= 3){
            let res = await fetch(`/api/course-selector/lfu?step=${_selected}&id=${dispatchData?.detail?.id}`);
            res = await res.json();
            if(res?.type === "CourseDetails"){
                let _groups = [];
                let data = res?.data;
                for(let courseType of data){
                    let res = await fetch(`/api/course-selector/lfu?step=5&id=${courseType?.id}`);
                    res = await res.json();
                    res.course = courseType.name;
                    _groups.push(res);
                    $groups = _groups;
                }
                selected = 4;
            }
        }
    }

    async function gotToStep(step){
        selected = step;
        $selectorSteps[$selectorSteps.length-1].currentStep = step;
        data = null;
        await initFetch();
    }

    async function addGroupToCalendar(group:any, course: any){
        //delete group from $groups 
        // for(let courseType of $groups){
        //     courseType.groups = courseType.groups.filter((g:any)=>g.number !== group.number);
        // }
        // $groups = [...$groups];

        for (let time of group?.times)
        {
            let event = {
                title: course.course + ":" + group.number,
                start: time.from,
                end: time.to,
            }  

            //check if event is already in events
            let isAlreadyInEvent = false;
            for(let e of events){
                if(e.title === event.title && e.start === event.start && e.end === event.end){
                    isAlreadyInEvent = true;
                    break;
                }
            }
            if(isAlreadyInEvent){
                addToast("Event already in calendar", "alert-error");
            }else{
                events = [...events, event];
            }
        }

        
        //if events have same time set background color to red
        events = events.map((event:any)=>{
            let count = 0;
            for(let e of events){
                if(e.start === event.start && e.end === event.end){
                    count++;
                }
            }
            if(count > 1){
                event.backgroundColor = "red";
            }
            return event;
        })

    }
    let groupTableHeaders = [
        "Group", "Date", "Time", "Location", "Comment", "AddToCalendar", "Details"
    ]
    $: console.log(events);
</script>


<section class="z-0">
    <div class=" justify-center w-full">
        <Steps bind:selected {gotToStep}/>
        <div class="mt-8 flex justify-center w-full">
            <SearchInput on:GET={nextStep} bind:data/>
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
