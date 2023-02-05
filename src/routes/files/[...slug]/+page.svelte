<script lang="ts">
    import folder from "$assets/folder.png"
    import MediaQuery from "$helper/MediaQuery.svelte";
    import Modal from "$components/general/Modal.svelte";

    import { page } from "$app/stores"
    import { filesLayoutStore } from '../filesLayoutStore';


    export let data:any; 
    let video:any = false;


    async function download(path: any){
        let response = await fetch(`${$page.url.pathname}/${path}`);
        let data = await response.blob();
        let url = URL.createObjectURL(data);
        
        if(path.includes(".mp4")){
            video = true;
            document.getElementById("videoId").setAttribute("src", url);//video tag id
            document.getElementById("videoId").play();//this is source tag id
            
        }else{
            const link = document.createElement('a');
            link.href = url;
            link.download = path;
            document.body.appendChild(link);
            link.click();
        }
        
        
    }
</script>


<section>
<MediaQuery query="(min-width: 590px)" let:matches>
    {#if matches}
        <!-- svelte-ignore a11y-media-has-caption -->
        <Modal open={video} on:close={()=> video = false}>
            <video on:submit|preventDefault={()=>console.log("Download")} on:ended={()=>video=false} id="videoId" controls/>
        </Modal>

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
                        <div class="flex p-2 hover:bg-base-300 rounded-xl w-full">
                            <i class="text-6xl bi bi-file-earmark-medical"></i>
                            <h1 class="flex items-center">{f}</h1>
                        </div>
                    </button>
                </div>
            {/each}
            </div>
        {/if}
        {#if $filesLayoutStore==="list"}
            <div class="grid grid-rows w-full">
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
                    <div class="w-full">
                        <!-- svelte-ignore a11y-click-events-have-key-events -->
                        <!-- svelte-ignore a11y-missing-attribute -->
                        <button class="cursor-pointer" on:click={()=>download(f)}>
                            <div class="flex p-2 hover:bg-base-300 rounded-xl w-full">
                                <i class="text-3xl bi bi-file-earmark-medical"></i>
                                <h1 class="flex items-center">{f}</h1>
                            </div>
                        </button>
                    </div>
                {/each}
            </div>
        {/if}
    {:else}
        <div class="grid grid-rows w-full">
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
                <div class="w-full">
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <!-- svelte-ignore a11y-missing-attribute -->
                    <button class="cursor-pointer" on:click={()=>download(f)}>
                        <div class="flex p-2 hover:bg-base-300 rounded-xl w-full">
                            <i class="text-xl bi bi-file-earmark-medical"></i>
                            <h1 class="flex items-center">{f}</h1>
                        </div>
                    </button>
                </div>
            {/each}
        </div>
    {/if}
</MediaQuery>

</section>