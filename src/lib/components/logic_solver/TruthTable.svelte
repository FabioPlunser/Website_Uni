<script lang="ts">
	// Input Variables
	export let input_names: String[];
	export let output_names: String[];
	export let editable: boolean = false;

	// Output Variables
	export let values: boolean[][];

	let num_inputs: number;
	$: num_inputs = input_names == null ? 0 : input_names.length;
	let num_outputs: number;
	$: num_outputs = output_names == null ? 0 : output_names.length;
	let v: boolean[][];
	$: v = Array.from({ length: num_outputs }, (_) =>
		new Array(2 ** num_inputs).fill(false)
	);

	$: values = v;

	let boolToString = (b: boolean) => (b ? "1" : "0");
</script>

{#if input_names != null && output_names != null}
	<table class="table-fixed border-seperate">
		<tr>
			{#each input_names as name}
				<th>{name}</th>
			{/each}
			{#each output_names as name}
				<th>{name}</th>
			{/each}
		</tr>
		{#each { length: 2 ** num_inputs } as _, row}
			<tr>
				{#each { length: num_inputs } as _, i}
					<td>
						{boolToString((row & (2 ** (num_inputs - 1 - i))) != 0)}
					</td>
				{/each}
				{#each { length: num_outputs } as _, i}
					{#if editable}
						<td
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
	</table>
{/if}
