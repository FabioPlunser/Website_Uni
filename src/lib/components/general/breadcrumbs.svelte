<script lang="ts">
    import {page} from "$app/stores";

    let crumbs = $page.url.pathname.split("/");
    crumbs = crumbs.filter((crumb) => crumb !== "");
    crumbs = [...crumbs];
</script>

<div class="text-sm max-w-xs md:max-w-none md:text-base md:font-bold breadcrumbs">
    <ul>
        {#each crumbs as crumb, i}
            <li>
                <a href="{$page.url.pathname.split("/", i+2).join("/")}">
                    <i class="hidden md:block bi bi-archive mx-1"></i>
                    {crumb = crumb.charAt(0).toUpperCase() + crumb.slice(1)}
                </a>
            </li>
        {/each}
    </ul>
</div>