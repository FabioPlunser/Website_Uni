<script lang="ts">
  export let group:any[] = null;
</script>


{#if group?.times.length < 1}
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
            {#each group?.times as time}
                <tr>
                    <td>{new Date(time.from).toLocaleString('de-De', { day: 'numeric',month: 'numeric', year: 'numeric'  })}</td>
                    <td>{time.time}</td>
                    <td>{new Date(time.from).toLocaleString('de-DE', {  weekday: 'short' })}</td>
                    <td>{time.location}</td>
                    <td>{time.comment}</td>
                </tr>
            {/each}
        </tbody>
      </table>
  </div>
{/if}

