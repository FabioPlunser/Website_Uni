import adapter from "@sveltejs/adapter-static";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: [
    preprocess({
      postcss: true,
    }),
  ],
  kit: {
    alias: {
      $src: "src",
      $lib: "src/lib",
      $components: "src/lib/components",
    },
    adapter: adapter({
      pages: "dist",
      assets: "dist",
      fallback: null,
      precompress: false,
    }),
    prerender: {
      // This can be false if you're using a fallback (i.e. SPA mode)
      default: true,
    },
  },
};

export default config;
