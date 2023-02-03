<script lang="ts">
	import Breadcrumbs from "$components/general/breadcrumbs.svelte"
	import { page } from "$app/stores"
	import { filesLayoutStore } from "./filesLayoutStore";
</script>

<div class="flex justify-between">
	<div class="flex items-center">
		{#key $page.url}
			<Breadcrumbs/>
		{/key}
	</div>

	<div class="hidden md:block gap-1 items-center">
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<i on:click={()=>$filesLayoutStore="list"} class="font-bold text-3xl bi bi-list p-4 rounded-xl {$filesLayoutStore==="grid" ? "text-gray-500 hover:bg-base-300" : "text-black dark:text-white"}"></i>
		<!-- svelte-ignore a11y-click-events-have-key-events -->
		<i on:click={()=>$filesLayoutStore="grid"} class="font-bold text-3xl bi bi-columns p-4 rounded-xl {$filesLayoutStore==="list" ? "text-gray-500 hover:bg-base-300" : "text-black dark:text-white"}"></i>
	</div>
</div>

<slot/>

