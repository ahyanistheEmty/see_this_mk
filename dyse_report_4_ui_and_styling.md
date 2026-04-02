### Report 4: User Interface and Styling

The user interface of Dyse is designed with a modern, clean aesthetic, supporting both light and dark themes, and leverages Tailwind CSS for utility-first styling.

**Styling Framework:**

*   **Tailwind CSS:** The `index.css` file imports `tailwindcss`, indicating that the project relies heavily on Tailwind's utility classes for responsive and efficient styling.
*   **Custom CSS Properties (CSS Variables):** A comprehensive set of CSS variables is defined in `:root` for managing application-wide styling, including:
    *   `--system-font`: For consistent typography.
    *   `--glass-opacity`: To control the transparency of "glassmorphism" effects.
    *   `--anim-speed`: To synchronize animation durations across the UI.
    *   Color variables for backgrounds (`--app-bg`, `--app-surface`, `--app-surface-elevated`, etc.), text (`--app-text-primary`, `--app-text-secondary`, `--app-text-muted`), borders (`--app-border`, `--app-border-strong`), hover states (`--app-hover-tint`), and overlays (`--app-overlay`).
    *   Shadow variables (`--app-shadow-soft`, `--app-shadow-strong`).
    *   Brand-specific colors (`--color-brand`, `--color-brand-hover`, `--color-brand-subtle`).
*   **Dark Mode Support:** The `:root[data-theme='dark']` block explicitly redefines many CSS variables to provide a distinct dark theme, ensuring a pleasant user experience in different lighting conditions.

**UI Components and Theming:**

*   **Themed Components:** Custom component styles are defined using `@layer components` in `index.css`, such as `theme-shell`, `theme-panel`, `theme-card`, `theme-chip`, `theme-input`, `auth-google-button`, `card-rounded`, `btn-pill`, `btn-primary`, `btn-secondary`, and `nav-item`. These classes abstract complex styling into reusable units, maintaining a consistent look and feel.
*   **Animations:** The CSS defines several `@keyframes` for animations, including:
    *   `spin-slow`, `liquid-shimmer`, `neural-pulse`: Likely for loading indicators or visual feedback.
    *   `tool-trace-bridge-draw`, `tool-trace-connector-draw`, `tool-trace-wrap-draw`, `tool-use-task-rise`: Suggest dynamic, animated elements for visualizing AI tool usage or task progress within the interface.
*   **Dynamic Theming in `App.tsx`:** The `App.tsx` component manages the `personality.themeMode` state and `systemThemeAtLaunch` to determine the active theme, applying it to the `document.documentElement`'s `data-theme` attribute. It also dynamically sets CSS properties like `--system-font`, `--glass-opacity`, and `--anim-speed` based on user personality settings.
