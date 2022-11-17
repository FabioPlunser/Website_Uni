<script lang="ts">
	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";

	let values: boolean[][];
	let input_names: String[];
	let output_names: String[];

	$: console.log(values);
</script>

<main class="m-5 w-full">
	<InputSelector bind:input_names bind:output_names />
	<TruthTable {input_names} {output_names} editable={true} bind:values />
</main>
