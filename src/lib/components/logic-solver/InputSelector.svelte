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
		<label for="NumInputs">Number of Inputs[1-6]:</label>
		<input
			class="input m-1"
			id="NumInputs"
			type="number"
			max=6
			min=1
			bind:value={num_inputs}
		/>
		<label for="NumOutputs">Number of Outputs[1-*]:</label>
		<input min=1 class="input m-1" id="NumOutputs" type="number" bind:value={num_outputs} />

		<div>
			<label for="InputSelectorModal" class="btn btn-primary">Edit Input/Output names</label>
		</div>
	</div>


	<input type="checkbox" id="InputSelectorModal" class="modal-toggle" />
	<label for="InputSelectorModal" class="modal cursor-pointer">
		<label class="modal-box relative" for="">
				<h1 class="font-bold text-lg">Edit Input/Output names</h1>
				<h3>Input names</h3>
				{#if input_names.length>0}
					{#each input_names as _, i}
						<input class="input m-1 bg-slate-600" type="text" bind:value={input_names[i]} />
					{/each}
				{/if}
				<h3>Output Names</h3>
				{#if output_names.length>0}
					{#each output_names as _, i}
						<input class="input m-1 bg-slate-600" type="text" bind:value={output_names[i]} />
					{/each}
				{/if}

				<div class="modal-action">
					<label for="InputSelectorModal" class="btn">Close</label>
				</div>
		</label>
	</label>


	<!-- <div class="flex flex-col flex-wrap">
		{#each input_names as name, idx}
			<label class="flex-1" for={"InputName" + idx}>Input Name {idx}:</label>
			<input class="flex-1 input m-1" id={"InputName" + idx} type="text" bind:value={name} />
		{/each}
	</div>


	<div class="flex flex-col flex-wrap">
		{#each output_names as name, idx}
			<label class="flex-1" for="OutputName {idx}">Output Name {idx}:</label>
			<input  class="flex-1 input m-1" id="OutputName {idx}" type="text" min=1 bind:value={name} />
		{/each}
	</div> -->
</main>
