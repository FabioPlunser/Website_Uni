<script lang="ts">
    export let headings:  string[] = [];
    export let data: { [key: string]: string }[] = [];
    export let maxCols: number = data.length;
    // $: console.log(data);
</script>   




<div class="overflow-x-auto rounded-lg">
    <table class="table  table-zebra w-full rounded-lg">
      <thead>
        <tr>
            {#each headings as heading}
                <th>{heading}</th>
            {/each}
        </tr>
      </thead>
      <tbody>
        {#each data as row}
            <tr class="w-full">
                {#each Object.values(row).slice(0, maxCols) as value}
                    <td class="break-all"><p class="break-all">{value}</p></td>
                {/each}
            </tr>
        {/each}
      </tbody>
    </table>
</div>