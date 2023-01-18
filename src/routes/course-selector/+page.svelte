<script lang="ts">
    import SearchInput from "$lib/components/general/SearchInput.svelte";

    enum Step {
        FieldOfStudy,
        Curriculum,
        CourseType,
        Group
    }
    $: console.log(selected);
    let selected = Step.FieldOfStudy;

    let data = [
        { name: "hallo",},        
        { name: "test",},        
        { name: "servus",},        
        { name: "hi",},        
    ]
</script>

<section>
    <div class="flex justify-center mx-auto items-center">
        {#if selected < 4}
            <ul class="steps"> 
                <li on:click={()=>selected=0} class="step {selected >= 0 && "step-primary"}">Choose field of Study</li>
                <li on:click={()=>selected=1} class="step {selected >= 1 && "step-primary"}">Choose curriculum</li>
                <li on:click={()=>selected=2} class="step {selected >= 2 && "step-primary"}">Choose course type</li>
                <li on:click={()=>selected=3} class="step {selected >= 3 && "step-primary"}">Choose group</li>
            </ul>  
        {/if}
    </div>
    <div class="flex justify-center">
        <SearchInput on:GET={()=>console.log("Get search value")} {data}/>
    </div>
    <button on:click={()=>selected++} class="btn btn-primary mt-5 flex mx-auto justify-center w-full max-w-xs">Next</button>
</section>
