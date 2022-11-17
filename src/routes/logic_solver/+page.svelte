<script lang="ts">
	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";
	import Algebra from "$components/logic_solver/algebra.svelte";
	let values: boolean[][];
	let input_names: String[];
	let output_names: String[];

</script>



<main class="m-5 w-full h-full">
	<div class="flex">
		<TruthTable {input_names} {output_names} editable={true} bind:values />
		<InputSelector bind:input_names bind:output_names />
		<Algebra {input_names} {output_names} {values}/>
	</div>

</main>


