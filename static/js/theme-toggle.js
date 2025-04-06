document.addEventListener("DOMContentLoaded", () => {
    const htmlRoot = document.getElementById("htmlRoot");
  
    if (
      localStorage.theme === "dark" ||
      (!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      htmlRoot.classList.add("dark");
    }
  
    window.toggleDarkMode = function () {
      htmlRoot.classList.toggle("dark");
      localStorage.theme = htmlRoot.classList.contains("dark") ? "dark" : "light";
    };
  });
  