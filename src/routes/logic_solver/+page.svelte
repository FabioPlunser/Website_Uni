<script lang="ts">
	import { browser } from "$app/environment";

	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";
	import Algebra from "$components/logic_solver/algebra.svelte";
	let values: boolean[][];
	let input_names: String[];
	let output_names: String[];

	function clearTable(){
		for(let i = 0; i < output_names.length; i++){
			for(let j = 0; j < 2 ** input_names.length; j++){
				values[i][j] = false;
			}
		}
	}
</script>



<main class="m-5 w-full h-full">
	<div class="flex">
		<div>
		<button class="btn btn-primary" on:click={()=>clearTable()} >Clear Table</button>
			<TruthTable {input_names} {output_names} editable={true} bind:values />
		</div>
		<InputSelector bind:input_names bind:output_names />
		<Algebra {input_names} {output_names} {values}/>
	</div>

</main>


