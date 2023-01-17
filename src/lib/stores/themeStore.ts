import { writable } from 'svelte/store';
import { browser } from '$app/environment';

const storedTheme = browser && localStorage.getItem('theme');
export const theme = writable(storedTheme || false);
theme.subscribe(value => {
    if(browser && value) {
        document.documentElement.setAttribute('data-theme', "dark");
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', value);
    }else if(browser && !value) {
        document.documentElement.setAttribute('data-theme', 'light');
        document.documentElement.classList.remove('dark');
        localStorage.removeItem('theme');
    }
});

