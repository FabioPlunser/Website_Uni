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

    export let LaTexCCNFS: string[] = [];
	export let LaTexCDNFS: string[] = [];

    let code = "";
    let latex_code = "";
    let latex_code2 = "";
    $: {
        latex_code = "";
        latex_code += "\\subsection{CCNFS}\n";
        for(let i = 0; i < LaTexCCNFS.length; i++){
            latex_code += "$" + LaTexCCNFS[i] + "$\\\\\n";
        }
        latex_code2 = "";
    }
    $: {
        latex_code2 = "";
        latex_code += "\\subsection{CDNFS}\n";
        for(let i = 0; i < LaTexCDNFS.length; i++){
            latex_code2 += "$" + LaTexCDNFS[i] + "$\\\\\n";
        }
    }

    $: {
        code = "";
        code += "\n"
        code += latex_code + latex_code2;
    }


    $: highlight = hljs.highlight("tex", code).value;
    async function copyToClipboard() {
        if (browser) {
            await navigator.clipboard.writeText(code);
            triggerToast();
        }
    }
</script>

<div id="LatexAlgebra" class="mockup-code">
    <button on:click={copyToClipboard} type="button" title="Copy Code" class="block ml-auto mr-2 -mt-10 hover:text-gray-600"><i class="text-3xl p-0 m-0 bi bi-file-code-fill"></i></button>
    <pre class="p-2"><code class="language-tex p-2">{@html highlight}</code></pre>
</div>

<style>
	@import 'https://unpkg.com/@highlightjs/cdn-assets@10.6.0/styles/atom-one-dark.min.css';
</style>

