<script lang="ts">
	import Spinner from '$components/courseSelector/spinner.svelte';
    import { getCourse } from "$src/lib/utils/fetchAPI";
    import { selectedCoursesStore } from "$lib/stores/selectedCourses";

    export let selectedCourseVarationID = 0;
    export let selectedCourseName = "";
    let groupSelected = false; 

    function handleSelect(groupData: any, courseID: any){
        
        if(groupSelected){
            $selectedCoursesStore = $selectedCoursesStore.filter(function(value, index, arr){
            if(value.courseID !== courseID){
                return value;
            }
            })

            groupSelected = false;
        }else{
            $selectedCoursesStore.forEach(function(value, index, arr){
                if(value.courseID === courseID){
                    groupSelected = true;
                    alert("Group already selected");
                    throw new Error("Group already selected");
                }
            
            })
            let events: any = [];
            for(let times of groupData.times){
                let timeSplit= times.time.split('-');
                let startSplit = timeSplit[0].trim().split('.');
                let startHour = +startSplit[0], startMinute = +startSplit[1];

                let endSplit = timeSplit[0].trim().split('.');
                let endHour = +endSplit[0], endMinute = +endSplit[1];

                let split = times.date.split('.');
                let year = +split[2], month = +split[1], day = +split[0];
                let start = new Date(year, month - 1, day, startHour, startMinute);
                let end = new Date(year, month - 1, day, endHour, endMinute);
                let event = {
                    start: start, 
                    end: end, 
                    title: selectedCourseName + " - Group " + groupData.number + " - " + times.comment,
                    group: groupData.number,
                };
                events = [...events, event];

            }
            
            
            groupSelected = true;
            $selectedCoursesStore = [...$selectedCoursesStore, {
                events: events,
                courseID: courseID,
            }];
        }
    }

</script>

{#await getCourse(selectedCourseVarationID, selectedCourseName)}
    <div class="flex justify-center mx-auto">
        <Spinner />
    </div>
{:then data} 
    <div class="w-auto mx-auto justify-center flex">
        <table class="table w-auto mx-auto">
            <thead>
                <tr>
                    <th>Group</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Location</th>
                    <th>Comment</th>
                    <th>Add to calendar</th>
                </tr>
            </thead>
            <tbody>
                {#each data.groups as group}
                    {#each group.times as times, i}     
                        <tr>
                            <th>{group.number}</th>
                            <td>{times.date}</td>
                            <td>{times.time}</td>   
                            <td>{times.location}</td>
                            <td>{times.comment}</td>
                            {#if i == 0}
                                {#if !groupSelected}
                                    <td><button on:click={()=>handleSelect(group, data.id)} class="btn btn-primary">Add Group {group.number} {selectedCourseName.slice(0,2)} to calendar</button></td>
                                {:else if groupSelected}
                                    <td><button on:click={()=>handleSelect(group, data.id)} class="btn btn-secondary">Remove from Calendar</button></td>
                                {/if}
                                    {:else}
                                    <td></td>
                            {/if}
                        </tr>
                    {/each}
                    <tr>
                        <th>---</th>
                        <td>---</td>
                        <td>---</td>
                        <td>---</td>
                        <td>---</td>
                        <td>---</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
{/await}