<script lang="ts">
    import folder from "$assets/folder.png"
    import { page } from "$app/stores"
    import { filesLayoutStore } from '../filesLayoutStore';
    export let data:any; 


    async function download(path: any){
        let response = await fetch(`${$page.url.pathname}/${path}`);
        let data = await response.blob();
        console.log(data);

        const url = URL.createObjectURL(data);
        const link = document.createElement('a');
        link.href = url;
        link.download = path;
        document.body.appendChild(link);
        link.click();
    }
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

            {#each data.files as f}
            <div>
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <!-- svelte-ignore a11y-missing-attribute -->
                <button class="cursor-pointer" on:click={()=>download(f)}>
                    <div class="flex p-2 hover:bg-base-300 rounded-xl">
                        <i class="text-6xl bi bi-file-earmark-medical"></i>
                        <h1 class="flex items-center">{f}</h1>
                    </div>
                </button>
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

            {#each data.files as f}
            <div>
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <!-- svelte-ignore a11y-missing-attribute -->
                <button class="cursor-pointer" on:click={()=>download(f)}>
                    <div class="flex p-2 hover:bg-base-300 rounded-xl">
                        <i class="text-3xl bi bi-file-earmark-medical"></i>
                        <h1 class="flex items-center">{f}</h1>
                    </div>
                </button>
            </div>
        {/each}
        </div>
    {/if}
</section>