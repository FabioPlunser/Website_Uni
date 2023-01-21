import { writable } from 'svelte/store';
import { Step } from '$types/enums';
import { browser } from '$app/environment';

interface SelectorStep {
    step: Step;
    id: number;
    [key: string]: any;
}

type SelectorSteps = SelectorStep[];

let data = [
    {step: 0, id: 0},
    {step: 1, id: 0},
    {step: 2, id: 0},
    {step: 3, id: 0},
    {currentStep: 0, id: 0},
]

export const course = writable([]);
export const groups = writable([]);
export const selectorSteps = writable<SelectorSteps>(data);