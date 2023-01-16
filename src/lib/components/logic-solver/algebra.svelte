<script lang="ts">
    export let values: boolean[][];
    export let input_names: String[];
	export let output_names: String[];
    $: num_inputs = input_names == null ? 0 : input_names.length;
	$: num_outputs = output_names == null ? 0 : output_names.length;
    export let CCNFS: string[] = [];
    export let CDNFS: string[] = [];
    export let LaTexCCNFS: string[] = [];
    export let LaTexCDNFS: string[] = [];
    
    $: {
        if(values != null && values.length >= num_outputs){
            CCNFS = [];
            CDNFS = [];
            LaTexCCNFS = [];
            LaTexCDNFS = [];
            for(let i = 0; i < num_outputs; i++){
                let CCNF = `${output_names[i]} = `;
                let CDNF = `${output_names[i]} = `;
                let LaTexCCNF = `${output_names[i]} = `;
                let LaTexCDNF = `${output_names[i]} = `;
                for(let j = 0; j <  Math.pow(2, num_inputs); j++){
                    if(values[i][j]){
                        CDNF += "(";
                        LaTexCDNF += "(";
                        for(let k = 0; k < num_inputs; k++){
                            if((j & (2 ** (num_inputs - 1 - k))) != 0){
                                CDNF += `<span>${input_names[k]}</span>`;
                                LaTexCDNF += `${input_names[k]}`;

                            }else{
                                CDNF += `<span class=\"overline\">${input_names[k]}</span>`;
                                LaTexCDNF += `\\overline{${input_names[k]}}`;

                            }
                            if(k != num_inputs - 1){
                                CDNF += "<span>∧<span>";
                                LaTexCDNF += " \\land ";
                            }
                        }
                        CDNF += ")";
                        LaTexCDNF += ")";
                        if(j != Math.pow(2, num_inputs) - 1){
                            CDNF += "<span>∨<span>";
                            LaTexCDNF += " \\lor ";

                            if(j % lineBreack == 1){
                                CDNF += "<br>";
                            }
                        }
                    }
                    if(!values[i][j]){
                        CCNF += "(";
                        LaTexCCNF += "(";
                        for(let k = 0; k < num_inputs; k++){
                            if((j & (2 ** (num_inputs - 1 - k))) != 0){
                                CCNF += `<span class=\"overline\">${input_names[k]}</span>`;
                                LaTexCCNF += `\\overline{${input_names[k]}}`;
                            }else{
                                CCNF += `<span>${input_names[k]}</span>`;
                                LaTexCCNF += `${input_names[k]}`;
                            }
                            if(k != num_inputs - 1){
                                CCNF += "<span>∨<span>";
                                LaTexCCNF += " \\lor ";
                            }
                        }
                        CCNF += ")";
                        LaTexCCNF += ")";
                        if(j != Math.pow(2, num_inputs) - 1){
                            CCNF += "<span>∧<span>";
                            LaTexCCNF += " \\land ";
                            if(j % lineBreack == 1){
                                CCNF += "<br>";
                            }
                        }
                    }
                }
                LaTexCCNFS.push(LaTexCCNF);
                LaTexCDNFS.push(LaTexCDNF);
                CCNFS.push(CCNF);
                CDNFS.push(CDNF);
                
            }
        }
    }

    let font = 20;
    let lineBreack = 2;
</script>


<div>
    <div>
        <label for="FontSizeAlgebra">Font Size</label>
        <input id="FontSizeAlgebra" class="input" type="number" min=5 max=48 bind:value={font}/>  
        <label for="LineBreakAlgebra">LineBreak</label>
        <input id="LineBreakAlgebra" class="input" type="number" min=2 max=10 bind:value={lineBreack}/>  
    </div> 
    <div style="font-size: {font + 'px'}" class="flex flex-col p-4 bg-gray-800 rounded-xl mt-2 flex-1 shadow-xl"> 
        CDNFS:
        {#each CDNFS as CDNF}
            <p>{@html CDNF}</p>
        {/each}


        CCNFS:
        {#each CCNFS as CCNF}
            <p>{@html CCNF}</p>
        {/each}
    </div>
    
</div>




