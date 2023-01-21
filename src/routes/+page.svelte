<script lang="ts">
    import transistor from "$assets/transistor.svg";
    import memori from "$assets/memori.svg";
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

    <div class="mt-24 flex flex-col sm:flex-row gap-10 justify-center">
        <div class="card w-auto bg-blue-200 dark:bg-primary shadow-2xl rotate-3 max-w-md">
            <div class="card w-auto bg-base-200 shadow text-black dark:text-white -rotate-3">
                <div class="card-body items-center text-center break-all">
                    <h2 class="card-title">Course Selector <i class="bi bi-calendar2-week"></i> </h2>
                    
                    <p>
                        A site to add courses to a simple Calendar to see if courses clash with each other 
                    </p>
                    <div class="card-actions justify-end">
                        <a href="/course-selector" class="btn btn-primary">Go</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="card w-auto bg-blue-200 dark:bg-primary shadow-2xl rotate-3 max-w-md">
            <div class="card w-auto bg-base-200 shadow text-black dark:text-white -rotate-3">
                <div class="card-body items-center text-center">
                    <h2 class="card-title">Logic Solver <img src={transistor} alt="logic solver logic" class="w-8 h-auto" /></h2>
                    <p>
                        A site where you can config a truth table and CCNF, DDNF and KV diagram are 
                        generated automatically
                    </p>
                    <div class="card-actions justify-end">
                        <a href="/logic-solver" class="btn btn-primary">Go</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="card w-auto bg-blue-200 dark:bg-primary shadow-2xl rotate-3 max-w-md">
            <div class="card w-auto bg-base-200 shadow-xl text-black dark:text-white -rotate-3">
                <div class="card-body items-center text-center">
                    <h2 class="card-title">Memori <img src={memori} alt="logic solver logic" class="w-8 h-auto" /></h2>
                    <p>
                        A site where you can create decks of flashcards and test yourself
                    </p>
                    <div class="card-actions justify-end">
                        <a href="/memori" class="btn btn-primary">Go</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>