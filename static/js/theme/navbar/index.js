document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "auto";
    setTheme(savedTheme);
});

const setTheme = (theme) => {
    if (theme === "auto") {
        theme = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }

    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);
    updateThemeIcon(theme);
    updateDropdownMenu(theme);
};

const updateThemeIcon = (theme) => {
    const themeIcon = document.getElementById("themeIcon");
    if (!themeIcon) return;

    const iconClasses = {
        dark: "bi bi-moon",
        light: "bi bi-brightness-high",
        auto: "bi bi-circle-half"
    };

    themeIcon.className = iconClasses[theme];
};

const updateDropdownMenu = (currentTheme) => {
    const dropdownMenu = document.getElementById("themeDropdownMenu");
    if (!dropdownMenu) return;

    const themes = {
        light: "bi bi-brightness-high",
        dark: "bi bi-moon",
        auto: "bi bi-circle-half"
    };

    dropdownMenu.innerHTML = ""; // Clear existing items

    Object.keys(themes).forEach((theme) => {
        if (theme !== currentTheme) {
            const menuItem = document.createElement("li");
            const link = document.createElement("a");
            link.href = "#";
            link.className = "dropdown-item theme-switch text-center";
            link.setAttribute("data-theme", theme);
            link.innerHTML = `<i class="${themes[theme]}"></i>`;

            link.addEventListener("click", (event) => {
                event.preventDefault();
                setTheme(theme);
            });

            menuItem.appendChild(link);
            dropdownMenu.appendChild(menuItem);
        }
    });
};
document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("bgVideo");

    if (video) {
        // Preload the video
        video.oncanplaythrough = () => {
            video.style.opacity = 1; // Fade in smoothly once loaded
        };

        // Cache video by using the browser's fetch API
        const videoSrc = video.querySelector("source").src;
        fetch(videoSrc, { cache: "force-cache" }).then(() => {
            console.log("Background video preloaded and cached.");
        }).catch(err => {
            console.warn("Video preloading failed:", err);
        });
    }
});