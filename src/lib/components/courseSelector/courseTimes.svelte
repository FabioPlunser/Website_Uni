<script lang="ts">
	import CourseTable from '$components/courseSelector/courseTable.svelte';
    let open = false;
    export let data:any;
</script>

<div class="relative w-auto overflow-hidden">
    <div class="bg-slate-800 h-12 w-full pl-5 flex items-center {open ? "rounded-t-lg" : "rounded-lg"}">
        <button on:click={()=> {open = !open}}><h1 class="text-lg underline">{data.name}</h1></button>
    </div>
    <div class="absolute top-3 right-3">
        <button on:click={()=> {open = !open}} class="transition-transform duration-200 {open ? "rotate-0" : "rotate-180"}"><i class="bi bi-caret-down"></i></button>
    </div>
    <div class="bg-slate-800 transition-all duration-500 pl-5 pb-5 rounded-b-lg {open ? "block" : "hidden"}">
        <CourseTable selectedCourseVarationID={data.id} selectedCourseName={data.name} />
    </div>
</div>