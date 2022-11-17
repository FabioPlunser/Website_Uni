<script lang="ts">
    import { browser } from '$app/environment';
    import { toastStore } from '@brainandbones/skeleton';
    import type { ToastSettings } from '@brainandbones/skeleton';
    function triggerToast(): void {
        const t: ToastSettings = {
            message: '👋 Copyed to clipboard',
            autohide: true,
            timeout: 2000,
            classes: 'bg-warning-500',
        };
        toastStore.trigger(t);
    }
                

    import hljs from 'highlight.js';

    export let values: boolean[][] = [];
    export let input_names: String[] = [];
	export let output_names: String[] = [];
    let num_inputs = 1; 
    let num_outputs = 1;
    $: if(input_names) num_inputs = input_names == null ? 1 : input_names.length;
	$: if(output_names) num_outputs = output_names == null ? 1 : output_names.length;



    let latex_code = "";
    $: console.log(values);
    $:{ 
        if(values.length > 0 && num_inputs > 0 && num_outputs > 0){
            latex_code = "\n";
            latex_code += "\\begin{tabular}{|";
            for(let i = 0; i < num_inputs; i++){
                latex_code += "c|";
            }
            for(let i = 0; i < num_outputs; i++){
                latex_code += "c|";
            }
            latex_code += "}\n";
            latex_code += "\\hline\n\t";
            for(let i = 0; i < num_inputs; i++){
                latex_code += input_names[i] + " & ";
            }
            for(let i = 0; i < num_outputs; i++){
                latex_code += output_names[i] + " & ";
            }
            latex_code += "\\\\ \\hline";
            for(let i = 0; i< (2**num_inputs); i++){
                latex_code += "\n\t";
                for(let j = 0; j < num_inputs; j++){
                    latex_code += (i & (1 << (num_inputs - 1 - j)) ? "1" : "0") + " & ";


                }
                for(let j = 0; j < num_outputs; j++){
                    try {
                        latex_code += (values[j][i] ? "1" : "0") + " & ";   
                    } catch (error) {
                        
                    }
                }
                latex_code += "\\\\ \\hline";
            }
            latex_code += "\n\\end{tabular}";
        }
    }
    $: highlight = hljs.highlight("tex", latex_code).value;
    async function copyToClipboard() {
        if (browser) {
            await navigator.clipboard.writeText(latex_code);
            triggerToast();
        }
    }
</script>

<div id="LatexTable" class="mockup-code">
    <button on:click={copyToClipboard} type="button" title="Copy Code" class="block ml-auto mr-2 -mt-10 hover:text-gray-600"><i class="text-3xl p-0 m-0 bi bi-file-code-fill"></i></button>
    <pre class="p-2"><code class="language-tex p-2">{@html highlight}</code></pre>
</div>

<style>
	@import 'https://unpkg.com/@highlightjs/cdn-assets@10.6.0/styles/atom-one-dark.min.css';
</style>

