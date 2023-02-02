<script lang="ts">
	import Breadcrumbs from "$components/general/breadcrumbs.svelte"
	import { page } from "$app/stores"
</script>

{#key $page.url}
	<Breadcrumbs/>
{/key}

<slot/>

