/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    
    "./static/**/*.{html,js}",

    "./templates/**/*.html",

    "./node_modules/tw-elements/dist/js/**/*.js"




],
  theme: {
    extend: {

      
    },
  },
  plugins: [
    require("tw-elements/dist/plugin.cjs")
  ],
}
