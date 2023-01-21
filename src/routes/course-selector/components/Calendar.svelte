<script lang="ts">
    let calendarDays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]
    let calendarHours = 12;
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
                    <td>{i+8}:00</td>
                    {#each Array(calendarDays.length) as _, j}
                        <td></td>
                    {/each}
                </tr>
            {/each}
        </tbody>
    </table>
</div>