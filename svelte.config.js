import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/kit/vite';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    alias: {
      $lib: "src/lib",
      $components: "src/lib/components",
      $helper: "src/lib/helper",
      $stores: "src/lib/stores",
      $types: "src/lib/types",
      $assets: "src/lib/assets",
    },
    adapter: adapter(),
  },
};

export default config;
