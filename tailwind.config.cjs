/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    "./node_modules/@brainandbones/skeleton/**/*.{html,js,svelte,ts}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
    require("flowbite/plugin"),
    require("@tailwindcss/typography"),
    require("tailwindcss-textshadow"),
    require("@brainandbones/skeleton/tailwind/theme.cjs"),
  ],
};
