<script lang="ts">
    import Calendar from '@event-calendar/core';
    import TimeGrid from '@event-calendar/time-grid';
    import { browser } from '$app/environment';

    export let events:any[] = [];
    $: console.log("calendar", events);
    let ec;
    let plugins = [TimeGrid];
    let options = {
        view: 'timeGridWeek',
        eventSources: [{events: function() {
            console.log('fetching...');
            return events;
        }}]
    };

    $: {
        if(browser && events.length > 0){
            invokeMethod();
            setDateToFirstArray();
        }
    }

    function setDateToFirstArray(){
        ec.setOption('date', new Date(events[0].start));
    }
    function invokeMethod() {
        ec.refetchEvents();
    }

</script>

<Calendar bind:this={ec} bind:plugins bind:options/>


<!-- <script lang="ts">
    let calendarDays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    let calendarHours = 16;
</script>

<div class="overflow-auto">
    <table class="table table-zebra w-auto broder-1">
        <thead>
            <tr>
                <th></th>
                {#each calendarDays as i}
                    <th>{i}</th>
                {/each}
            </tr>
        </thead>
        <tbody>
            {#each Array(calendarHours) as _, i}
                <tr>
                    {#if (i+6) < 10}
                        <td>0{i+6}:00</td>
                    {:else}
                        <td>{i+6}:00</td>
                    {/if}
                    {#each Array(calendarDays.length) as _, j}
                        <td></td>
                    {/each}
                </tr>
            {/each}
        </tbody>
    </table>
</div> -->
