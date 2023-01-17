<script lang="ts">


    enum Step {
        FieldOfStudy,
        Curriculum,
        CourseType,
        Group
    }
    $: console.log(selected);
    let selected = Step.FieldOfStudy;
</script>

<section>
    <div class="flex justify-center mx-auto items-center">
        {#if selected < 4}
            <ul class="steps"> 
                <li class="step {selected===Step.FieldOfStudy && "step-primary"}">Choose field of Study</li>
                <li class="step {selected===Step.Curriculum && "step-primary"}">Choose curriculum</li>
                <li class="step {selected===Step.CourseType && "step-primary"}">Choose course type</li>
                <li class="step {selected===Step.Group && "step-primary"}">Choose group</li>
            </ul>  
        {/if}
    </div>
    <input type="text" placeholder="Type Here" class="mt-20 flex mx-auto justify-center input w-full bg-base-300 max-w-xs" />
    <button on:click={()=>selected++} class="btn btn-primary mt-5 flex mx-auto justify-center w-full max-w-xs">Next</button>
</section>
