<script lang="ts">
	// Input Variables
	export let input_names: String[];
	export let output_names: String[];
	export let editable: boolean = false;

	export let boolToString: (b: boolean) => string = (b: boolean) => {
		return b ? "1" : "0";
	};

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
</script>

{#if num_inputs > 0 && num_outputs > 0}
	<div class="flex overflow-x-auto">
		>>>>>>> origin/dev
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
								{boolToString(
									(row & (2 ** (num_inputs - 1 - i))) != 0
								)}
							</td>
						{/each}
						{#if editable}
							{#each { length: num_outputs } as _, i}
								<td
									class="cursor-pointer hover:text-gray-500"
									on:click={(_) =>
										(values[i][row] = !values[i][row])}
								>
									{boolToString(values[i][row])}
								</td>
							{/each}
						{:else}
							{#each { length: num_outputs } as _, i}
								<td class="hover:text-gray-500">
									{boolToString(values[i][row])}
								</td>
							{/each}
						{/if}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{:else}
	<p>Cannot create Truth Table without Inputs or Outputs.</p>
{/if}
