<script lang="ts">
    import SideBar from "$src/lib/components/sideBar.svelte";
    import "../app.css";
</script>

<div class="text-white bg-slate-900 dark flex">
    <div class="">
        <SideBar />
    </div>
     <slot/>
</div>
