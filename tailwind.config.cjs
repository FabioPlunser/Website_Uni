/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
  ],
  darkMode: "class",
  theme: {},

  plugins: [
    require("daisyui"),
    require("flowbite/plugin"),
    require("@tailwindcss/typography"),
    require("tailwindcss-textshadow"),
  ],
};
