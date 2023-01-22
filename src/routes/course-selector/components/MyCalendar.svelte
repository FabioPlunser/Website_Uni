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

    let events = [
        {day: "Monday", time: "6:00", name: "Math", duration: 2},
    ];

    function addEvent(event) {
        events = [...events, event];
    }

    function removeEvent(event) {
        events = events.filter(e => e !== event);
        events = [...events];
    }

</script>

<div id="calendar" class="bg-base-300 rounded-xl w-fit shadow-xl p-5">
    <div class="overflow-x-auto">
        <table class="w-full">
            <thead>
            <tr>
                <th class="text-center py-2 px-2 border-2 border-gray-500 dar:border-white w-1/8">Time:</th>
                {#each week as day}
                <th class="text-center py-2 px-2 border-2 border-gray-500 dar:border-white w-1/8">{day}</th>
                {/each}
            </tr>
            </thead>
            <tbody>
                {#each {length: 17} as _, i}
                    <tr>
                        <td class="text-center py-2 px-2 border-2 border-gray-500 dar:border-white w-1/8">{i+6}:00</td>
                        {#each week as day}
                            <td class="text-center py-2 px-2 border-r-2 border-b-2 border-gray-500 dar:border-white w-1/8">
                                {#each events as event, j}
                                    {#if event.day === day && event.time === `${i+6}:00`}
                                        <div out:fly={{y: 50, duration: 200}} on:click={()=>removeEvent(event)} class="bg-blue-300 -my-4 flex justify-center p-2 z-[{j}] rounded-lg absolute max-h-min" style="height: {event.duration*58}px;">
                                            {event.name}
                                        </div>
                                    {/if}
                                {/each}
                            </td>
                        {/each}
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>
