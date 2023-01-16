<script lang="ts">
  	import Select from 'svelte-select';

    export let bindto: any;
    export let data: any; 
    export let text = "";

    let items:any[] = [];
    data.data.forEach(element => {
      let label = element.id + " " + element.name.slice(0,80);
      items.push({value: element.id, label: label});
    });
    
    function handleSelect(event: any){
      bindto = event.detail.label;
    }
</script>

<!-- <select bind:value={bindto} class="select w-full max-w-xs mx-auto flex justify-center">
    <option disabled selected>{text}</option>       
    {#each data.data as data}
      <option>{data.id} {data.name.slice(0, 80)}</option>
    {/each}
</select> -->

<div class="theme">
  <Select {items} placeholder={text} on:select={handleSelect}/>
</div>


<style>
	.theme{
		--background: rgb(43, 48, 59) !important;
    --border: 0px;
    --placeholderColor: white;
		--listBackground: rgb(43, 48, 59);
		--itemHoverColor: rgb(255, 255, 255); 
		--itemHoverBG: rgb(37, 37, 37);
    --borderRadius: 10px;
    --listZIndex: 100;
    --inputFontSize: 1.5rem;
    font-size: small;
	}
</style>