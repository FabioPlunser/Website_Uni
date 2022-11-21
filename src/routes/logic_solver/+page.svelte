<script lang="ts">
	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";
	import KvMap from "$components/logic_solver/KvMap.svelte";
	import Algebra from "$components/logic_solver/algebra.svelte";
	import Latextable from "$components/logic_solver/latextable.svelte";
	import Latexalgebra from "$src/lib/components/logic_solver/latexalgebra.svelte";

	let values: boolean[][];
	let input_names: String[];
	let output_names: String[];

	let CCNFS: string[];
	let CDNFS: string[];
	let LaTexCCNFS: string[];
	let LaTexCDNFS: string[];

	function clearTable() {
		for (let i = 0; i < output_names.length; i++) {
			for (let j = 0; j < 2 ** input_names.length; j++) {
				values[i][j] = false;
			}
		}
	}
</script>

<div class="sticky top-0 z-50 flex justify-center mx-auto">
	<div class="bg-slate-600 w-full bg-base-100 mb-5 shadow-xl">
		<a class="btn btn-ghost normal-case text-xl" href="#TruthTable"
			>Truth Table</a
		>
		<a class="btn btn-ghost normal-case text-xl" href="#KV">KV Diagramm</a>
		<a class="btn btn-ghost normal-case text-xl" href="#LatexTable"
			>LatexTable</a
		>
		<a class="btn btn-ghost normal-case text-xl" href="#LatexAlgebra"
			>LatexAlgebra</a
		>
	</div>
</div>

<main class=" w-full h-full overflow-auto justify-center mx-auto">
	<div class="m-10">
		<div id="TruthTable" class="flex">
			<div>
				<button class="btn btn-primary" on:click={() => clearTable()}
					>Clear Table</button
				>
				<TruthTable
					id="Table"
					{input_names}
					{output_names}
					editable={true}
					bind:values
				/>
			</div>
			<InputSelector bind:input_names bind:output_names />
			<Algebra
				{input_names}
				{output_names}
				{values}
				bind:CCNFS
				bind:CDNFS
				bind:LaTexCCNFS
				bind:LaTexCDNFS
			/>
		</div>
		<div class="flex">
			<div class="max-h-min max-w-min m-2">
				<Latextable {input_names} {output_names} {values} />
			</div>
			<div class="max-w-lg m-2">
				<Latexalgebra {LaTexCCNFS} {LaTexCDNFS} />
			</div>
		</div>
	</div>
</main>
