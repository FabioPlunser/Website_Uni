<script lang="ts">
    import { navStore } from "$lib/stores/navStore";
    $navStore = [
        {text: "Course Selector", href: "/course-selector"},
        {text: "Logic Solver", href: "/logic-solver"},
        {text: "Memory", href: "/memori"},
    ]
</script>

<section>
    <div class="flex items-center justify-center">
        <div class="card w-96 bg-base-100 shadow-xl">
            <div class="card-body">
                <h1 class="font-bold">Landing page</h1>
            </div>
        </div>
    </div>
</section>