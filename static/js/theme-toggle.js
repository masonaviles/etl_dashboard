// static/js/theme-toggle.js

document.addEventListener("DOMContentLoaded", function () {
    const htmlRoot = document.getElementById("htmlRoot");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const theme = localStorage.theme || (prefersDark ? "dark" : "light");
  
    if (theme === "dark") {
      htmlRoot.classList.add("dark");
    }
  
    window.toggleDarkMode = function () {
      htmlRoot.classList.toggle("dark");
      localStorage.theme = htmlRoot.classList.contains("dark") ? "dark" : "light";
    };
  });
  