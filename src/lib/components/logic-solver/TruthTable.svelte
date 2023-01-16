<script lang="ts">


	// Input Variables
	export let input_names: String[];
	export let output_names: String[];
	export let editable: boolean = false;

	// Output Variables
	export let values: boolean[][];

	// State Tracker
	$: v /*: boolean[][] */ = Array.from({ length: num_outputs }, (_) =>
		new Array(2 ** num_inputs).fill(false)
	);

	$: num_inputs /* : number*/ = input_names == null ? 0 : input_names.length;
	$: num_outputs /* : number */ =
		output_names == null ? 0 : output_names.length;

	function boolToString(b: boolean): String {
		return b ? "1" : "0";
	}

	$: values = v;

	
</script>

{#if input_names != null && output_names != null}
	<div class="flex overflow-x-auto text-white">
		<table class="table table-zebra table-fixed border-seperate">
			<thead>
				<tr>
					{#each input_names as name}
						<th>{name}</th>
					{/each}
					{#each output_names as name}
						<th>{name}</th>
					{/each}
				</tr>
			</thead>
			<tbody>
				{#each { length: 2 ** num_inputs } as _, row}
					<tr class="hover rounded-ld">
						{#each { length: num_inputs } as _, i}
							<td>
								{boolToString((row & (2 ** (num_inputs - 1 - i))) != 0)}
							</td>
						{/each}
						{#each { length: num_outputs } as _, i}
							{#if editable}
								<td class="cursor-pointer hover:text-gray-500"
									on:click={(e) => (values[i][row] = !values[i][row])}
								>
									{boolToString(values[i][row])}
								</td>
							{:else}
								<td>
									{boolToString(values[i][row])}
								</td>
							{/if}
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{/if}

