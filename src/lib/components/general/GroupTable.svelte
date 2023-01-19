<script lang="ts">
    export let group:any[];

    $: console.log(group);

    let dateObj = null;
    for(let time of group.times){
        let date = time.date; 
        let dateParts = date.split(".");

        let englishDate = dateParts[2] + '/' + dateParts[1]  + '/' + dateParts[0];
        dateObj = new Date(englishDate);
    }
</script>


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
        {#each group.times as time}
            <tr>
                <td>{dateObj.toLocaleString('de-De', { day: 'numeric',month: 'numeric', year: 'numeric'  })}</td>
                <td>{time.time}</td>
                <td>{dateObj.toLocaleString('de-DE', {  weekday: 'short' })}</td>
                <td>{time.location}</td>
                <td>{time.comment}</td>
            </tr>
        {/each}
      </tbody>
    </table>
</div>