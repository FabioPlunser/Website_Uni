<script lang="ts">
    import folder from "$assets/folder.png"
    import { page } from "$app/stores"
	import { filesLayoutStore } from './filesLayoutStore';

    export let data:any; 
</script>


<section>
    {#if $filesLayoutStore==="grid"}
        <div class="grid grid-cols-5">
            {#each data.folders as f}
                <div>
                    <a href="{$page.url.pathname}/{f}">
                        <div class="flex hover:bg-base-300 rounded-xl">
                            <img src={folder} alt="folder" class="w-20 h-auto" />
                            <h1 class="flex items-center">{f}</h1>
                        </div>
                    </a>
                </div>
            {/each}
        </div>
    {/if}
    {#if $filesLayoutStore==="list"}
        <div class="grid grid-rows">
            {#each data.folders as f}
                <div>
                    <a href="{$page.url.pathname}/{f}">
                        <div class="flex hover:bg-base-300 rounded-xl">
                            <img src={folder} alt="folder" class="w-12 h-auto" />
                            <h1 class="flex items-center">{f}</h1>
                        </div>
                    </a>
                </div>
            {/each} 
        </div>
    {/if}
</section>