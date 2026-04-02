### Report 2: Development Environment and Dependencies

The `dyse` project utilizes a modern JavaScript/TypeScript development stack with several key dependencies for its functionality and build process.

**Core Dependencies:**

*   **AI/ML:** `@google/genai`, `openai` for AI model interactions.
*   **Frontend Frameworks:** `react`, `react-dom`, `@react-three/fiber`, `three` (for 3D rendering/visualizer).
*   **Backend/Server:** `express`, `cors`, `dotenv`, `googleapis` (for Google API interactions), `playwright`, `playwright-extra`, `puppeteer-extra-plugin-stealth` (for browser automation).
*   **Database/Auth:** `@supabase/supabase-js`, `express-session` for user authentication and data persistence.
*   **UI/Styling:** `tailwindcss`, `@tailwindcss/vite`, `lucide-react` (for icons), `motion` (for animations).
*   **Desktop Integration:** `electron`, `screenshot-desktop`, `open`, `tsx` (for running TypeScript directly).

**Development Dependencies:**

*   `typescript` (for type checking).
*   `vite`, `@vitejs/plugin-react` (for fast development server and build).
*   `electron-builder` (for packaging desktop applications).
*   `concurrently`, `wait-on` (for running multiple processes).
*   `sharp` (for image processing, likely for optimizations or visual assets).

**Environment Configuration (`.env.example`):**
The project expects environment variables for:
*   Application URLs (`APP_URL`, `VITE_API_BASE_URL`, `ALLOWED_ORIGINS`).
*   Security (`SESSION_SECRET`, `GOOGLE_TOKEN_ENCRYPTION_KEY`).
*   API Keys/Secrets for Google, GitHub, Supabase, and Gemini (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`, `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`, `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `GEMINI_API_KEY`, `GEMINI_API_KEYS`, `DESKTOP_API_KEY`).
*   Hosted Gemini usage limits (`HOSTED_GEMINI_WINDOW_HOURS`, `HOSTED_GEMINI_WINDOW_FREE_UNITS`).

**Ignored Files (`.gitignore`):**
Includes standard ignores for development artifacts, node modules, environment files, logs, and Electron build outputs, ensuring a clean repository.
