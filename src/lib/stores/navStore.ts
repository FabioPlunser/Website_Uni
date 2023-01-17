import { writable } from 'svelte/store';
import type { NavButtons } from '$lib/types';

export const navStore = writable<NavButtons>([]);
