<svelte:head>
    <title>Uni Olat</title>
</svelte:head>

<script lang="ts">
    import {login, logout} from '$lib/helper/fetchAPI';
    import { error } from "@sveltejs/kit";

    let username = '';
    let password = '';
    let data:any[] = [];
    let sessionid = "";
    async function localLogin(){
        let res = await fetch("http://localhost:3002/api/login", {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: username, password: password})
            })
        let res2 = await res.json()
        console.log(res2);
        sessionid = res2.session;
    }
    $: console.log(sessionid);
    
</script>

<div class="flex justify-center mx-auto">
    <div>
        <input class="input w-full max-w-xs m-2" type="text" bind:value={username} placeholder="Username"/>
        <input class="input w-full max-w-xs m-2" type="password" bind:value={password} placeholder="Password"/>
    </div>
    <br/>
    <button class="btn btn-primary" on:click={()=>localLogin()}>Login</button>

</div>


{#await data}
    <div class="flex mx-auto justify-center">
        <div class="spinner"></div>
    </div>
{:then data}
    {#each data as course}
        <h1>{course}</h1> 
    {/each}
{/await}