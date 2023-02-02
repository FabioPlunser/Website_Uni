<script lang="ts">
    import folder from "$assets/folder.png"
    import { page } from "$app/stores"
    export let data:any; 
    // console.log(data);
    // console.log("page", $page.url.pathname);
    async function testing(path: any){
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
                <a on:click={()=>testing(f)} target="_blank">
                    <div class="flex p-2 hover:bg-base-300 rounded-xl">
                        <i class="text-6xl bi bi-file-earmark-medical"></i>
                        <h1 class="flex items-center">{f}</h1>
                    </div>
                </a>
            </div>
        {/each}

    </div>
</section>