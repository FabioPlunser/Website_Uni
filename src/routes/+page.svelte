<script lang="ts">
    import transistor from "$assets/transistor.svg";
    import memori from "$assets/memori.svg";
    import IndexCards from "$components/general/IndexCards.svelte";
</script>

<section>
    <div class="flex items-center justify-center">
        <div class="font-bold text-2xl text-center">
            <h1>UIBK Help</h1>
            <span>
                A website to help students 
                pick their courses and provide 
                nice to haves, especially for computer science students
            </span>
        </div>
        
      
    </div>
    
    <div class="mt-24 grid grid-rows sm:grid-cols-2 md:grid-cols-3  gap-10 justify-center">
            <IndexCards>
                <h2 class="card-title">Course Selector <i class="bi bi-calendar2-week"></i> </h2>
                <p>
                    A site to add courses to a simple Calendar to see if courses clash with each other 
                </p>
                <div class="card-actions justify-end">
                    <a href="/course-selector" class="btn btn-primary">Go</a>
                </div>
            </IndexCards>

       <div class="opacity-50">
            <IndexCards>
                <h2 class="card-title">Logic Solver <img src={transistor} alt="logic solver logic" class="w-8 h-auto" /></h2>
                <h1 class="text-3xl">Under development</h1>
                <!-- <p>
                    A site where you can config a truth table and CCNF, DDNF and KV diagram are 
                    generated automatically
                </p>
                <div class="card-actions justify-end">
                    <a href="/logic-solver" class="btn btn-primary">Go</a>
                </div> -->
            </IndexCards>
        </div>

        <div class="opacity-50">
            <IndexCards>
                <h2 class="card-title">Memori <img src={memori} alt="logic solver logic" class="w-8 h-auto" /></h2>
                <h1 class="text-3xl">Under planing</h1>
                <!-- <p>
                    A site where you can create decks of flashcards and test yourself
                </p>
                <div class="card-actions justify-end">
                    <a href="/memori" class="btn btn-primary">Go</a>
                </div> -->
            </IndexCards>
        </div>
       
        <div class="opacity-50">
            <IndexCards>
                <h2 class="card-title">Tutorials <i class="bi bi-question-circle-fill w-8 h-auto"></i></h2>
                <h1 class="text-3xl">Under planing</h1>
                <!-- <p>
                Some tutorials for students. For example how to setup latex and using it in vscode. 
                Some cheatsheets.
                </p>
                <div class="card-actions justify-end">
                    <a href="/memori" class="btn btn-primary">Go</a>
                </div> -->
            </IndexCards>
        </div>

        <IndexCards>
            <h2 class="card-title">Files <i class="bi bi-archive-fill w-8 h-auto"></i></h2>
            <p>
                Here you can find some files that are useful for students. 
                For example some templates for latex or some proseminar homework.
            </p>
            <div class="card-actions justify-end">
                <a href="/files" class="btn btn-primary">Go</a>
            </div>
        </IndexCards>

        
    </div>
</section>