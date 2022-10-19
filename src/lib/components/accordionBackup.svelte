<script lang="ts">
	import CourseTable from './courseTable.svelte';
	import Select from '$components/select.svelte';
    let open = false;
    export let title = "";
    export let content = "";
    export let courseVarationID: number;


    import { getLFUID } from "$lib/helper/fetchAPI";
    import Spinner from "$components/spinner.svelte";
    let selectedCourseVaration = "";
    let selectedCourseVarationID = 0;
    let selectedCourseName = "";
    $: selectedCourseVarationID= parseInt(selectedCourseVaration.split(" ")[0]);
    $: selectedCourseName = selectedCourseVaration.replace(selectedCourseVarationID + " ", "");
</script>

<div class="relative w-auto overflow-hidden">
    <div class="bg-slate-800 h-12 w-full pl-5 flex items-center {open ? "rounded-t-lg" : "rounded-lg"}">
        <button on:click={()=> {open = !open}}><h1 class="text-lg">{title}</h1></button>
    </div>
    <div class="absolute top-3 right-3">
        <button on:click={()=> {open = !open}} class="transition-transform duration-200 {open ? "rotate-0" : "rotate-180"}"><i class="bi bi-caret-down"></i></button>
    </div>
    <div class="bg-slate-800 transition-all duration-500 pl-5 pb-5 rounded-b-lg {open ? "block" : "hidden"}">
        <p>{content}</p>  

        <br class="mt-4"/>
        {#if courseVarationID != 0}
            {#await getLFUID(courseVarationID)}
                <div class="flex justify-center mx-auto">
                    <Spinner />
                </div>
            {:then data}
                <Select bind:bindto = {selectedCourseVaration} data={data} text="Select Course Variation" />
            {:catch error}
                <p>{error}</p>
            {/await}
        {/if}

        <br class="mt-4"/>
        {#if selectedCourseVaration.length > 1}
            <div class="flex justify-center mx-auto">
                <CourseTable selectedCourseVarationID={selectedCourseVarationID}  selectedCourseName={selectedCourseName}/>
            </div>
        {/if}
       

        <div class="flex justify-end p-1">
            <button class="btn btn-primary text-sm">Go to calender</button>
        </div>
    </div>
</div>