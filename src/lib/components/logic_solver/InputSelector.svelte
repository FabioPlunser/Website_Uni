<script lang="ts">
	// Output Variables
	export let num_inputs: number = 2;
	export let num_outputs: number = 1;

	export let input_names: String[] = Array.from(
		{ length: num_inputs },
		(_, i) => genInputName(i)
	);
	export let output_names: String[] = Array.from(
		{ length: num_outputs },
		(_, i) => genOutputName(i)
	);

	$: input_names = ToLen<String>(input_names, num_inputs, genInputName);
	$: output_names = ToLen<String>(output_names, num_outputs, genOutputName);

	function genInputName(idx: number) {
		return "x" + idx;
	}
	function genOutputName(idx: number) {
		return "y" + idx;
	}
	function ToLen<a>(arr: a[], len: number, gen: (idx: number) => a): a[] {
		let diff = len - arr.length;
		if (diff > 0) {
			return arr.concat(
				Array.from({ length: diff }, (_, i) => gen(len - diff + i))
			);
		} else if (diff < 0) {
			return arr.slice(0, len);
		}4
		return arr;
	}
</script>

<main class="m-5 flex  flex-row">
	<div class="flex flex-col">
		<label for="NumInputs">Number of Inputs:</label>
		<input
			class="input m-1"
			id="NumInputs"
			type="number"
			max="6"
			min="1"
			bind:value={num_inputs}
		/>
		<label for="NumOutputs">Number of Outputs:</label>
		<input class="input m-1" id="NumOutputs" type="number" bind:value={num_outputs} />
	</div>
	

	<div class="flex flex-col">
		{#each input_names as name, idx}
			<label for={"InputName" + idx}>Input Name {idx}:</label>
			<input class="input m-1" id={"InputName" + idx} type="text" bind:value={name} />
		{/each}
	</div>


	<div class="flex flex-col">
		{#each output_names as name, idx}
			<label for="OutputName {idx}">Output Name {idx}:</label>
			<input class="input m-1" id="OutputName {idx}" type="text" bind:value={name} />
		{/each}
	</div>
</main>
