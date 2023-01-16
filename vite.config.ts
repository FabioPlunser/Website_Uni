import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';


const config: UserConfig = {
	plugins: [sveltekit()],
	resolve: {
		dedupe: ['@fullcalendar/common'],
	},
	optimizeDeps: {
		include: ['@fullcalendar/common', "highlight.js", "highlight.js/lib/core"],
	}
};

export default config;
