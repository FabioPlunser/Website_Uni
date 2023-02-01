<!-- <script lang="ts">
	import { createEventDispatcher } from 'svelte';
    let dispatch = createEventDispatcher();
    import { browser } from '$app/environment';
    import { course, groups } from "$stores/selectorSteps";

    import Modal from "$components/general/Modal.svelte";
    import Table from "$components/general/Table.svelte"
    import Calendar from '@event-calendar/core';
    import TimeGrid from '@event-calendar/time-grid';

    let showEvent = false;
    let group:any = null;
    let ModalInfo:any = null;
    let headings = [
        "Date", 
        "Time",
        "Location",
        "Comment"
    ];
    export let events:any[] = [
        {
            title: 'Event 1',
            start: '2023-01-23T10:00:00',
            end: '2023-01-23T12:00:00'
        },
    ];
    $: console.log("calendar", events);
    let ec;
    let plugins = [TimeGrid];
    let options = {
        view: 'timeGridWeek',
        eventSources: [{events: function() {
            console.log('fetching...');
            return events;
        }}],
        eventClick: handleModal,
    };

    $: {
        if(browser && events.length > 0){
            invokeMethod();
            setDateToFirstArray();
        }
    }

    function setDateToFirstArray(){
        if(ec) ec.setOption('date', new Date(events[0].start));
    }
    function invokeMethod() {
       if(ec) ec.refetchEvents();
    }

    function handleDelete(info:any){
        if(ec) ec.removeEventById(info.event.id);
        dispatch("delete", info.event.title);
        console.log(info);
    }

    function clearCalendar(){
        events = [];
        invokeMethod();
    }

    function handleModal(info:any){
        console.log($groups)
        console.log(info.event.title.split(" "));
        console.log(info.event.title.split(":"));
        
        for(let courseType of $groups){
            if(courseType.course.includes(info.event.title.split(" ")[0])){
                for(let g of courseType.groups){
                    if(g.number === parseInt(info.event.title.split(":")[1])){
                        console.log(g);
                        group = g;
                    }
                }
            }
        }
        ModalInfo = info;
        console.log("group", group);
        showEvent = true;
    }

</script>
<div class="flex justify-center">
    <button class="flex justify-center btn btn-primary " on:click={()=>clearCalendar()}>Clear Calendar</button>
</div>
<!-- <Calendar bind:this={ec} bind:plugins bind:options on:dateClick={handleDelete} on:click={()=>console.log("click")}/> -->


<!-- {#if showEvent}
    <Modal open={showEvent} on:close={()=>showEvent = false}>
        <h1 class="flex justify-center text-2xl font-bold">Group: {group.number}</h1>
        <div class="p-4">
            <Table {headings} data={group.times} maxCols={4}/>
        </div>
        <div class="modal-action">
            <button class="btn btn-primary" on:click={()=>showEvent = false}>Close</button>
            <button class="btn btn-primary" on:click={()=>handleDelete(ModalInfo)}>Delete Event</button>
        </div>
    </Modal>
{/if} --> -->