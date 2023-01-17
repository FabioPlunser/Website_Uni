/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
  ],
  darkMode: "class",
  theme: {},

  plugins: [
    require("@tailwindcss/typography"),
    require("daisyui"),
    require("flowbite/plugin"),
    require("tailwindcss-textshadow"),
  ],
  daisyui: {
    themes: [ "light", "dark" ],
  },
};
