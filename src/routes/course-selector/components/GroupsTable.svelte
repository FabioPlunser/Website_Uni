<script lang="ts">
  export let groups:any[] = null;
  export let parOfArray:number = 0;

  
  $: console.log("groups", groups);

  let finished = false;
 
  convertTimes();

  async function convertTimes(){
    for(let group of groups){
      if(group.times.length < 1){
        return;
      }
      let times:any = [];
      for(let time of group.times){
        let fromDate = time.date; 
        let toDate = time.date;

        let fromDateParts = fromDate.split(".");
        let toDateParts = toDate.split(".");


        let fromTime = time.time.split("-")[0];
        let toTime = time.time.split("-")[1];

        let fromTimeParts = fromTime.split(".");
        let toTimeParts = toTime.split(".");
        
        
        let englishFromDate = fromDateParts[2] + '/' + fromDateParts[1]  + '/' + fromDateParts[0];
        let englishToDate = toDateParts[2] + '/' + toDateParts[1]  + '/' + toDateParts[0];

        let from = new Date(englishFromDate);
        from.setHours(fromTimeParts[0]);
        from.setMinutes(fromTimeParts[1]);
        let to = new Date(englishToDate);
        to.setHours(toTimeParts[0]);
        to.setMinutes(toTimeParts[1]);
  


        times.push({
          from: from,
          to: to,
          time: time.time,
          location: time.location,
          comment: time.comment
        });
      }
      group.times = times;
      console.log("groupTimes", group.times);
    }
    groups=[...groups];
    finished = true;

  }
  console.log(groups[0].times[0].from.toLocaleString('de-De', { day: 'numeric', month: 'numeric', year: 'numeric' }));
</script>

{#if finished}
<div class="grid gap-4">
{#each groups as group}
  <div>
    {#if group.times.length < 1}
      <div class="text-center">
        <p class="text-2xl font-bold">No times found</p>
      </div>
    {:else}
      <div class="overflow-x-auto">
          <table class="table table-zebra w-full">
            <thead>
              <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Day</th>
                <th>Location</th>
                <th>Comment</th>
              </tr>
            </thead>
            <tbody>
              {#if parOfArray !== 0}
                {#each group?.times.splice(0, parOfArray) as time}
                    <tr>
                        <td>{time.from.toLocaleString('de-De', { day: 'numeric', month: 'numeric', year: 'numeric'  })}</td>
                        <td>{time.time}</td>
                        <td>{time.from.toLocaleString('de-DE', {  weekday: 'short' })}</td>
                        <td>{time.location}</td>
                        <td>{time.comment}</td>
                    </tr>
                {/each}
              {:else}
                {#each group?.times as time}
                    <tr>
                        <td>{time.from.toLocaleString('de-De', { day: 'numeric',month: 'numeric', year: 'numeric'  })}</td>
                        <td>{time.time}</td>
                        <td>{time.from.toLocaleString('de-DE', {  weekday: 'short' })}</td>
                        <td>{time.location}</td>
                        <td>{time.comment}</td>
                    </tr>
                {/each}
              {/if}
            </tbody>
          </table>
      </div>
    {/if}
  </div>
{/each}
</div>
{/if}
