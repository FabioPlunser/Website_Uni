<script lang="ts">
    import {page} from "$app/stores";

    let crumbs = $page.url.pathname.split("/");
    crumbs = crumbs.filter((crumb) => crumb !== "");
    crumbs = [...crumbs];
</script>

<div class="font-bold breadcrumbs">
    <ul>
        {#each crumbs as crumb, i}
            {#if crumb.includes(".")}
                <li>
                    <a href="{$page.url.pathname.split("/", i+2).join("/")}">
                        <i class="bi bi-file-earmark-fill"></i>
                        {crumb = crumb.charAt(0).toUpperCase() + crumb.slice(1)}
                    </a>
                </li>
            {:else}
                <li>
                    <a href="{$page.url.pathname.split("/", i+2).join("/")}">
                        <i class="bi bi-archive mx-1"></i>
                        {crumb = crumb.charAt(0).toUpperCase() + crumb.slice(1)}
                    </a>
                </li>
            {/if}
        {/each}
    </ul>
</div>