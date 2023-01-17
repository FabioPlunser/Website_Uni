import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const storedTheme = browser && localStorage.getItem('theme');
export const theme = writable(storedTheme || 'light');
theme.subscribe(value => {
    if(browser) {
        document.documentElement.setAttribute('data-theme', value);
        if(value === 'light') document.documentElement.classList.remove('dark');
        else document.documentElement.classList.add('dark');
        localStorage.setItem('theme', value);
    };  
});

