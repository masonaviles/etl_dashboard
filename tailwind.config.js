/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './analyzer/templates/**/*.html',
      './templates/**/*.html',
    ],
    darkMode: ['class', '.dark-mode'],
    theme: {
      extend: {},
    },
    plugins: [],
    safelist: [
      'bg-white', 'text-indigo-700', 'rounded-xl', 'shadow',
      'text-sm', 'text-xl', 'font-semibold', 'font-medium',
      'md:col-span-2', 'p-4', 'mb-2', 'mt-2',
      'dark:bg-gray-700', 'dark:text-white', 'hover:bg-indigo-200',
      'dark:hover:bg-indigo-600', 'bg-gray-50', 'text-gray-800', 'font-sans'
    ]
}
  