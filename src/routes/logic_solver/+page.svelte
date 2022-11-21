<script lang="ts">
	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";
	import KvMap from "$components/logic_solver/KvMap.svelte";

	let values: boolean[][];
	let input_names: String[];
	let output_names: String[];
</script>

<main class="m-5">
	<InputSelector bind:input_names bind:output_names />
	<TruthTable {input_names} {output_names} editable={true} bind:values />
	<KvMap
		values={[true, true, false, true]}
		{input_names}
		show_position={true}
	/>
</main>
