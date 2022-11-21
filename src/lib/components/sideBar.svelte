<script lang="ts">
    let sideBar = false;
</script>


<aside class="absolute min-h-screen h-screen z-50 overflow-scroll {sideBar ? "w-auto md:min-max-ift" : "w-12"} md:text-xl" aria-label="Sidebar">
    <div class="overflow-y-auto py-4 px-2 rounded bg-gray-800 h-screen {sideBar ? "w-auto" : "w-12"} md:text-xl md:px-0" >
       <ul class="space-y-2">     
            <li>
                <button class="ml-2" on:click={() => {sideBar = !sideBar}}>
                    <i class="bi bi-list cursor-pointer {sideBar ? "rotate-90" : ""} duration-100 md:text-xl"></i>
                </button>
            </li>  
            <li>
                <a href="/" class="flex items-center p-2 text-base font-normal rounded-lg text-white hover:bg-gray-100 hover:bg-gray-700 md:text-xl">
                    <i class="bi bi-house"></i>
                    <span class="ml-3 {sideBar ? "" : "hidden"}">Home</span>
                </a>
            </li>   
            <li>
                <a href="/courseSelector" class="flex items-center p-2 text-base font-normal rounded-lg text-white hover:bg-gray-100 hover:bg-gray-700 md:text-xl">
                    <i class="bi bi-calendar-week"></i>
                    <span class="ml-3 {sideBar ? "" : "hidden"}">CourseSelector</span>
                </a>
            </li>
            <li>
                <a href="/logic_solver" class="flex items-center p-2 text-base font-normal rounded-lg text-white hover:bg-gray-100 hover:bg-gray-700 md:text-xl">
                    <i class="bi bi-calendar-week"></i>    
                    <span class="ml-3 {sideBar ? "" : "hidden"}">KV Solver</span>
                </a>
            </li>
            <li>
                <a href="/courseSelector" class="flex items-center p-2 text-base font-normal rounded-lg text-white hover:bg-gray-100 hover:bg-gray-700 md:text-xl">
                    <i class="bi bi-calendar-week"></i>
                    <span class="ml-3 {sideBar ? "" : "hidden"}">Better OLAT</span>
                </a>
            </li>
            
       </ul>
       <ul> 
        <li>
            <a href="/about" class="flex items-center p-2 text-base font-normal rounded-lg text-white hover:bg-gray-100 hover:bg-gray-700 md:text-xl">
                <i class="bi bi-person"></i>
                <span class="ml-3 {sideBar ? "" : "hidden"}">About</span>
        </li>
       </ul>
    </div>
 </aside>
 