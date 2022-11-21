/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    require("path").join(
      require.resolve("@brainandbones/skeleton"),
      "../**/*.{html,js,svelte,ts}"
    ),
  ],
  darkMode: "class",
  theme: {},

  plugins: [
    require("daisyui"),
    require("flowbite/plugin"),
    require("@tailwindcss/typography"),
    require("tailwindcss-textshadow"),
    require("@brainandbones/skeleton/tailwind/theme.cjs"),
  ],
};
