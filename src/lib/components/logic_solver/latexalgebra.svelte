<script lang="ts">
    import { browser } from '$app/environment';
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

<div class="max-w-fit bg-stone-900 p-2 rounded-xl">
    <button on:click={copyToClipboard} type="button" title="Copy Code" class="block ml-auto mr-2 hover:text-gray-600"><i class="text-3xl p-0 m-0 bi bi-file-code-fill"></i></button>
    <div class="overflow-auto">
        <pre class="p-2"><code class="language-tex p-2">{@html highlight}</code></pre>
    </div>
</div>

<style>
	@import 'https://unpkg.com/@highlightjs/cdn-assets@10.6.0/styles/atom-one-dark.min.css';
</style>

