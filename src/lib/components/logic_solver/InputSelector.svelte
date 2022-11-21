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
		}
		return arr;
	}
</script>

<main class="m-5">
	<!-- TODO: Make Labels/Inputs reusable? -->
	<label for="NumInputs">Number of Inputs:</label>
	<input
		id="NumInputs"
		type="number"
		max="6"
		min="1"
		bind:value={num_inputs}
	/>

	<br />

	<label for="NumOutputs">Number of Outputs:</label>
	<input id="NumOutputs" type="number" bind:value={num_outputs} />

	<br />

	{#each input_names as name, idx}
		<br />
		<label for={"InputName" + idx}>Input Name {idx}:</label>
		<input id={"InputName" + idx} type="text" bind:value={name} />
	{/each}

	<br />

	{#each output_names as name, idx}
		<br />
		<label for={"OutputName" + idx}>Output Name {idx}:</label>
		<input id={"OutputName" + idx} type="text" bind:value={name} />
	{/each}
</main>
