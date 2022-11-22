<script lang="ts">
    // #TODO Redo design add to website.
    import {getLFU, getLFUID } from "$lib/helper/fetchAPI";
    import Spinner from "$components/courseSelector/spinner.svelte";
    import Select from '$components/courseSelector/select.svelte';
	  import Accordion from '$src/lib/components/courseSelector/accordion.svelte';
	  import CourseTimes from '$components/courseSelector/courseTimes.svelte';



    import { onMount } from 'svelte';
	  import { Calendar} from '@fullcalendar/core';
    import { CalendarApi, CalendarRoot } from "@fullcalendar/common";
    import adaptivePlugin from '@fullcalendar/adaptive';
    import interactionPlugin from '@fullcalendar/interaction';
    import daygridPlugin from '@fullcalendar/daygrid';
    import listPlugin from '@fullcalendar/list';
    import timegridPlugin from '@fullcalendar/timegrid';
    import resourceTimelinePlugin from '@fullcalendar/resource-timeline';

    let options = {
      themeSystem: 'bootstrap5',
      initialView: 'timeGridWeek',
      height: 300,
      width: "auto",
      contentHeight: "auto",
      plugins: [
        adaptivePlugin, interactionPlugin, daygridPlugin,
        listPlugin, timegridPlugin, resourceTimelinePlugin
      ],
      editable: false,
      headerToolbar: {
        left: 'today prev,next',
        center: 'title',
        right: 'resourceTimelineDay,timeGridWeek,dayGridMonth,listWeek,listYear'
      },
      buttonText: {
        today: 'Jump to Today',
        prev: 'Previous',
        next: 'Next',
        day: 'Day',
        week: 'Week',
        month: 'Month',
        listWeek: 'List Week',
        listYear: 'List Year'
      },
      slotEventOverlap: false,
      allDaySlot: false,
      slotDuration: { minutes: 15 },
      slotLabelInterval: { hours: 1 },
      slotMinTime: { hours: 8 },
      scrollTime: { hours: 8 },
      scrollTimeReset: false,
      slotMaxTime: { hours: 20 },
      schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
      resourceAreaHeaderContent: 'Rooms',
      resources: [],
    };

    let classes: string; 
    let style: string;
    let calendarEl: any;
    let calendar: Calendar;
    let calendarAPI: CalendarApi = new CalendarApi();
    onMount(async () => {
      await import("@fullcalendar/core/vdom.js");
      if(!canBeInitiated) return;
      initCalendar();
      return() => {
        calendar && calendar.destroy();
      };
    })
   
    $: canBeInitiated =
      options &&
      options.plugins &&
      options.plugins.length &&
      calendarEl &&
      !calendar;
    let calendarInitiated = false;

    $: {
      if (calendar && options && options.plugins && options.plugins.length)
        updateCalendarOptions();

      if (canBeInitiated) {
        initCalendar();
        calendarInitiated = true;
      }
    }
    function initCalendar() {
      calendar = new Calendar(calendarEl, options);
      calendar.render();
	  }
    function updateCalendarOptions() {
      calendar.pauseRendering();
      calendar.resetOptions(options);
      calendar.resumeRendering();
    }
    



    let selectedFaculty = "";
    let selectedFacultyID = 0;
    $: selectedFacultyID = parseInt(selectedFaculty.split(" ")[0], 10);

    let selectedCurriculum = "";
    let selectedCurriculumID = 0;
    $: selectedCurriculumID = parseInt(selectedCurriculum.split(" ")[0], 10);

    let selectedCourseCategory = "";
    let selectedCourseCategoryID = 0;
    $: selectedCourseCategoryID = parseInt(selectedCourseCategory.split(" ")[0], 10);

    import { selectedCoursesStore } from "$lib/stores/selectedCourses";

    let hideCourses = false;
    let eventCount = 0;
    $: {
      if(calendarInitiated){
        calendar.removeAllEvents();
        for (let course of $selectedCoursesStore) {
          console.log(course);
          for (let event of course.events){
            calendar.addEvent(event);
            eventCount++;
          }
        } 
      }
    }
    
    function clearCalendar(){
      $selectedCoursesStore = [];
      calendar.removeAllEvents();
    }
</script>


<main class="m-5">
    <h1 class="underline text-4xl justify-center mx-0 flex mb-12">Course Selector</h1>
    <div class="grid grid-cols-3 gap-2">
      {#await getLFU()}
        <div class="flex justify-center mx-auto">
          <Spinner />
        </div>
      {:then data}
        <Select bind:bindto={selectedFaculty} data={data} text="Select Faculty" />
      {:catch error}
        <p>{error}</p>
      {/await}

      
      {#if selectedFaculty.length > 1}
        {#await getLFUID(selectedFacultyID)}
          <div class="flex justify-center mx-auto">
            <Spinner />
          </div>
        {:then data}
          <Select bind:bindto = {selectedCurriculum} data={data} text="Select Curriculum" />
        {/await}
      {/if}


      {#if selectedCurriculum.length > 1}
        {#await getLFUID(selectedCurriculumID)}
          <div class="flex justify-center mx-auto">
            <Spinner />
          </div>
        {:then data}
          <Select bind:bindto = {selectedCourseCategory} data={data} text="Select course type" />
        {/await}
      {/if}

      
    </div>  

    <br class="h-5"/>
    <!-- <div class="flex"> -->
      {#if selectedCourseCategory.length > 1}
        <div class="divider"><button on:click={()=>hideCourses = !hideCourses} class="btn {hideCourses ? "btn-secondary" : "btn-primary"}">Hide Courses</button></div>
        <div class="{hideCourses ? "hidden" : "block"}">
            {#await getLFUID(selectedCourseCategoryID)}
              <div class="flex justify-center mx-auto">
                <Spinner />
              </div>
            {:then data}
              {#if data.type === "CourseDetails"}
                {#each data.data as course}
                  <div class="p-2">
                    <CourseTimes data={course}/>
                  </div>
                {/each}
              {:else}
                {#each data.data as data}
                  <div class="p-2">
                    <Accordion title={data.name.slice(0, 80)} content={data.name} courseVarationID={data.id}/>
                  </div>
                {/each}
              {/if}
            {/await}
        </div>
      {/if}
      {#if $selectedCoursesStore.length > 0}
        <div class="divider"><button on:click={()=>clearCalendar()} class="btn btn-primary">Clear Calendar</button></div>
      {/if}




      <div id="button" class="mx-auto h-1/3">
        <div bind:this={calendarEl} class={classes} {style} />
      </div>
    <!-- </div> -->
</main>
