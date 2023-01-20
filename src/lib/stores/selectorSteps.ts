import { writable } from 'svelte/store';
import { Step } from '$types/enums';
import { browser } from '$app/environment';

interface SelectorStep {
    step: Step;
    id: number;
}

type SelectorSteps = SelectorStep[];

let data = [
    {step: 0, id: 0},
    {step: 1, id: 0},
    {step: 2, id: 0},
    {step: 3, id: 0},
    {step: 4, id: 0},
    {step: 5, id: 0},
    {step: 6, id: 0},

]

const local = browser ? localStorage.getItem('selectorSteps') : null;
export const selectorSteps = writable<SelectorSteps>(JSON.parse(local) ||data);
selectorSteps.subscribe(value => {
    browser && (localStorage.setItem('selectorSteps', value));
});