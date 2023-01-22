<script lang="ts">
    import { slide, fly } from "svelte/transition";
    const week = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ];

    export let events = [
        {day: "Monday", time: "12:00", name: "Mathe", duration: 2},

    ];
    $: console.log("calendar", events);
    $: events = [...events];

    function addEvent(event) {
        events = [...events, event];
    }

    function removeEvent(event) {
        events = events.filter(e => e !== event);
        events = [...events];
    }

    $: {
        for(let event of events){
            console.log(event.time.split(":"));
        }
    }

</script>

<div id="calendar" class="bg-base-300 rounded-xl shadow-xl p-5 w-full">
    <div class="overflow-x-auto w-full">
        <table class="w-full rounded-xl border-2 border-gray-500">
            <thead class="rounded-xl">
            <tr>
                <th class="text-center py-2 px-2 border-2 rounded-xl  border-gray-500 w-auto">Time:</th>
                {#each week as day}
                <th class="text-center py-2 px-2 border-2 rounded-xl border-gray-500 w-auto">{day}</th>
                {/each}
            </tr>
            </thead>
            <tbody>
                {#each {length: 17} as _, i}
                    <tr>
                        <td class="text-center py-2 px-2 border-2 border-gray-500 w-auto">{i+6}:00</td>
                        {#each week as day}
                            <td class="text-center py-2 px-2 border-r-2 border-b-2 border-gray-500 w-auto">
                                <div class="flex">
                                    {#key events}
                                        {#each events as event, j}
                                            {#if event.day === day && event.time.split(":")[0] === `${i+6}`}
                                                <!-- svelte-ignore a11y-click-events-have-key-events -->
                                                <div out:fly={{y: 50, duration: 200}} on:click={()=>removeEvent(event)} class="bg-blue-300 -my-4 mx-[{j}] flex justify-center p-2 z-[{j*10}] absolute rounded-lg max-h-min max-w-[{150-j}px] break-all overflow-hidden" style="height: {event.duration*58}px; max-height: {event.duration*58}px;">
                                                    {event.name}
                                                </div>
                                            {/if}
                                        {/each}
                                    {/key}
                                </div>
                            </td>
                        {/each}
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>
