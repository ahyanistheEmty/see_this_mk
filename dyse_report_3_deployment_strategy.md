### Report 3: Deployment and Hosting Strategy

The `dyse` project provides clear guidelines for deploying both its web and desktop versions, emphasizing cloud services for the web and local execution for desktop-specific features.

**Website Deployment (e.g., Render/Vercel):**

*   **Build and Start Commands:** `npm install` followed by `npm run build` to create the production frontend assets, and `npm run server:only` to run the Express backend.
*   **Environment Variables:** Extensive use of environment variables is crucial for configuring API keys, OAuth secrets, Supabase connections, and application URLs. Key variables include: `NODE_ENV=production`, `SKIP_VITE=true` (to ensure the built frontend is served), `APP_URL`, `VITE_ENABLE_PROJECTS=false`, `VITE_ENABLE_DESKTOP=false` (explicitly disabling desktop features for web).
*   **Shared AI Capacity:** `GEMINI_API_KEYS` is used to allow Dyse to rotate across multiple Gemini API keys for hosted chat, enhancing availability.
*   **Supabase Integration:** Detailed steps for setting up a Supabase project, enabling Google as an Auth provider, configuring redirect URLs, and running SQL scripts for chat sessions, hosted Gemini usage, Google integrations, and GitHub integrations. The `SUPABASE_SERVICE_ROLE_KEY` is required for secure account deletion and quota management.
*   **OAuth Callbacks:** Specific callback URLs are required for Google and GitHub OAuth to ensure proper authentication flow (`/api/auth/google/callback`, `/api/auth/github/callback`).
*   **User-Configured Integrations:** n8n API URL and Key are to be configured per user within Dyse settings, not as deployment-wide environment variables, offering more flexibility.

**Desktop-Only Features:**

*   The `DEPLOYMENT.md` explicitly states that "local filesystem access," "local shell/command execution," "Windows desktop screenshots and automation," "device-specific desktop agent behavior," and "project workspace UI and local project tools" should remain desktop-only. This means these functionalities are not intended for the web release and require a desktop/Electron distribution or a separate always-on backend.
*   The `App.tsx` file uses `import.meta.env.VITE_ENABLE_PROJECTS` and `VITE_ENABLE_DESKTOP` to conditionally enable/disable features based on the build target, reinforcing the distinction between web and desktop capabilities.
