/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './analyzer/templates/**/*.html',
        './etl_dashboard/templates/**/*.html',
        './templates/**/*.html',
        './**/*.py',
      ],      
    darkMode: 'class',
    theme: {
      extend: {},
    },
    plugins: [],
}
  