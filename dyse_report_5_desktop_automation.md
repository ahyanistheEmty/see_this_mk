### Report 5: Desktop Agent and Automation Capabilities

Dyse is designed with advanced desktop integration and automation features, particularly for its Windows desktop application, allowing the AI to interact with the local environment and external services.

**Desktop Agent (Windows Specific):**

*   **`personality.desktopAgentEnabled`:** This setting in `App.tsx` controls whether the Desktop Agent features are active, indicating an opt-in mechanism for users. The `DEPLOYMENT.md` also notes that desktop features are "opt-in per user/device inside Dyse settings and is disabled by default."
*   **`ComputerUse` Module:** `App.tsx` includes a `ComputerUse` module that displays screenshots of the system and a "neural cursor," indicating that the AI can visually perceive and interact with the desktop environment.
*   **`runDesktopAgent`:** A function in `App.tsx` that sends tasks to the backend for execution in the desktop environment. It handles starting and stopping a visual "glow" effect, and reports step-by-step progress (`DesktopAgentStep[]`).
*   **PowerShell Scripts (`glow.ps1`, `agent_hud.ps1`):**
    *   `glow.ps1`: A PowerShell script designed to create a visual "glow" border around the screen, likely to provide a visual cue to the user when the desktop agent is active. It allows customization of color, thickness, blur, and pulse speed.
    *   `agent_hud.ps1`: This file is empty, but its name suggests an intention for a PowerShell-based "agent heads-up display" or additional desktop utility, which may be a future feature or a placeholder.
*   **`electron-main.js` (Backend Integration):** The Electron main process spawns a local server (`server.ts`, inferred backend) which is responsible for executing desktop actions. This highlights the communication channel between the Electron frontend and the local system for automation.
*   **`executeComputerAction`, `executeSystemAction`:** Functions in `App.tsx` to interact with the computer's browser and system, including navigation, taking screenshots, and performing tasks.

**General Automation and Tooling:**

*   **Ghost Worker (`runGhostWorker`):** A background worker that executes tasks using direct API access to Google Workspace (Gmail, Drive, Calendar) and n8n workflow automation, without requiring UI interaction. This allows for silent, efficient automation.
*   **n8n Engine:** A specialized mode of the `Ghost Worker` for creating and executing n8n workflows, which requires user-configured n8n API URL and Key.
*   **Integrated AI Tools:** Dyse integrates various tools through `handleToolCall`, including:
    *   **Google Workspace:** `list_gmail_messages`, `read_gmail_message`, `send_gmail_message`, `list_drive_files`, `read_drive_file`, `create_drive_file`, `delete_drive_file`, `list_google_docs`, `read_google_doc`, `create_google_doc`, `update_google_doc`, `list_google_sheets`, `read_google_sheet`, `create_google_sheet`, `update_google_sheet`, `list_calendar_events`, `create_calendar_event`, `delete_calendar_event`.
    *   **GitHub:** `list_github_repositories`, `get_latest_github_repository`, `get_github_repository_overview`, `create_github_repository`, `read_github_repository_file`, `upsert_github_repository_file`, `upsert_github_repository_files`.
    *   **Local File System:** `create_local_folder`, `create_local_file`, `read_local_file`, `list_local_files`, `run_local_command`, `set_active_workspace`, `close_workspace`.
    *   **Visual Generation:** `render_visual` (for image synthesis).
    *   **Web Search:** `googlesearch` (leveraging Gemini's built-in Google Search grounding).
*   **Tool Authorization:** The `App.tsx` includes logic (`userExplicitlyRequestedToolAction`, `getHostedCapabilityBlockerMessage`) to ensure user intent and necessary API scopes are present before executing sensitive actions like desktop control or external service interactions.
