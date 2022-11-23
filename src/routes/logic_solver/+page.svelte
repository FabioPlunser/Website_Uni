<script lang="ts">
	import TruthTable from "$components/logic_solver/TruthTable.svelte";
	import InputSelector from "$components/logic_solver/InputSelector.svelte";
	import Algebra from "$components/logic_solver/algebra.svelte";
	import Latextable from "$src/lib/components/logic_solver/LatexTable.svelte";
	import Latexalgebra from "$src/lib/components/logic_solver/LatexAlgebra.svelte";

	import Accordion from "$components/ui/accordion.svelte";

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

<main class="w-full h-full overflow-auto justify-center mx-auto text-white">
	<div class="mx-5 m-2" id="KV-Diagramm">
		<Accordion title="Truth Table">
			<div id="TruthTable" class="mx-auto md:m-0 md:flex">
				<div class="mx-auto md:m-0">
					<InputSelector bind:input_names bind:output_names />
					<button
						class="btn btn-primary ml-5 mx-auto"
						on:click={() => clearTable()}>Clear Table</button
					>
				</div>
				<div class="mx-auto md:m-0">
					<TruthTable
						id="Table"
						{input_names}
						{output_names}
						editable={true}
						bind:values
					/>
				</div>
			</div>
		</Accordion>
	</div>
	<div class="mx-5 m-2" id="Algbera">
		<Accordion title="Algebra">
			<Algebra
				{values}
				{input_names}
				{output_names}
				bind:CCNFS
				bind:CDNFS
				bind:LaTexCCNFS
				bind:LaTexCDNFS
			/>
		</Accordion>
	</div>
	<div class="mx-5 m-2" id="KV-Diagramm">
		<Accordion title="KV-Diagramm" />
	</div>
	<div class="mx-5 m-2" id="Latex Code">
		<Accordion title="Latex Code">
			<div class="mx-auto justify-center">
				<div class="mx-auto flex justify-center">
					<Latexalgebra {LaTexCCNFS} {LaTexCDNFS} />
				</div>
				<br class="m-2" />
				<div class="mx-auto flex justify-center">
					<Latextable {values} {input_names} {output_names} />
				</div>
			</div>
		</Accordion>
	</div>
	<div class="mx-5 m-2" id="SVG Circuit">
		<Accordion title="SVG Circuit" />
	</div>
	<!-- <div class="m-10"> -->
	<!-- <Algebra {input_names} {output_names} {values} bind:CCNFS bind:CDNFS bind:LaTexCCNFS bind:LaTexCDNFS/> -->
	<!-- <div class="flex">

<div class="max-h-min max-w-min m-2">

<Latextable  {input_names} {output_names} {values} />

</div>

<div class="max-w-lg m-2">

<Latexalgebra {LaTexCCNFS} {LaTexCDNFS} />

</div>
                </div> -->
	<!-- </div>		 -->
</main>
