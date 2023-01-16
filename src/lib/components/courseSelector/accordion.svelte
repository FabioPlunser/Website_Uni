<script lang="ts">
	import CourseTimes from '$components/courseSelector/courseTimes.svelte';
    import Spinner from "$components/courseSelector/spinner.svelte";
    import { getLFUID } from '$src/lib/utils/fetchAPI';

    let open = false;
    export let title = "";
    export let content = "";
    export let courseVarationID: number;
</script>

<div class="relative w-auto overflow-hidden" on:click={()=> {open = !open}}>
    <div class="bg-slate-800 h-12 w-full pl-5 flex items-center {open ? "rounded-t-lg" : "rounded-lg"}" on:click={()=> {open = !open}}>
        <button on:click={()=> {open = !open}}><h1 class="text-lg">{title}</h1></button>
    </div>
    <div class="absolute top-3 right-3">
        <button on:click={()=> {open = !open}} class="transition-transform duration-200 {open ? "rotate-0" : "rotate-180"}"><i class="bi bi-caret-down"></i></button>
    </div>
    <div class="bg-slate-800 transition-all duration-500 pl-5 pb-5 rounded-b-lg {open ? "block" : "hidden"}">
        <p>{content}</p>  

        <!-- <p>{courseVarationID}</p> -->
        {#if courseVarationID != 0}
            {#await getLFUID(courseVarationID)}
                <div class="flex justify-center mx-auto">
                    <Spinner />
                </div>
            {:then data}
                {#each data.data as course}
                    <CourseTimes data={course} />
                {/each}
            {:catch error}
                <p>{error}</p>
            {/await}
        {/if}

        {#if courseVarationID == 0}
            <h1 class="text-red-600">Course is not available in this semester</h1>
        {/if}
       

        <div class="flex justify-end p-1">
            <a href="#button"><button class="btn btn-primary text-sm">Go to calender</button></a>
        </div>
    </div>
</div>