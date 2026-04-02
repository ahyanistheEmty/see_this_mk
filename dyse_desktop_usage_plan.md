# Dyse Agent: Plan for Enhanced Desktop Usage Abilities

This document outlines a detailed plan to enhance and fully enable desktop usage abilities for the Dyse agent, building upon the existing Electron and React infrastructure.

## Current State Analysis

Based on the review of `App.tsx`, `electron-main.js`, `index.tsx`, `agent_hud.ps1`, and `glow.ps1`:

*   **Core Application (`App.tsx`):**
    *   The application already includes state management (`Desktop Agent State`, `Computer Use State`) and functions (`runDesktopAgent`, `stopDesktopAgent`, `executeComputerAction`, `runComputerAgent`) that interact with backend API endpoints (`/api/system/*`, `/api/computer/*`). This signifies that the *framework* for desktop and browser automation is largely in place.
    *   The `getSystemInstruction` function explicitly defines the desired capabilities for the `DESKTOP AGENT`, stating it "can control the mouse, keyboard, open apps, run shell commands, use the clipboard, AND use the Playwright browser — all in one unified agent loop." This is a critical blueprint for the desired functionality.
    *   It uses `execute_ui_action` for actions like `EXECUTE_DESKTOP_TASK` and `EXECUTE_BROWSER_TASK`, indicating a structured approach to agent tool calls.
    *   A `CommandConfirmationModal` exists, suggesting user approval is required for `run_local_command`, which is a good security measure.
    *   Activation is dependent on the `VITE_ENABLE_DESKTOP` environment variable being `true` and the application running in a local environment (`IS_LOCAL_RUNTIME`).
*   **Electron Main Process (`electron-main.js`):**
    *   This file is responsible for launching the Electron application and, crucially, spawning a backend server process (`server.ts`). This `server.ts` file (whose content was not directly available) is inferred to be the primary handler for desktop interactions, as Electron's renderer process is sandboxed.
    *   It manages the Electron window and the lifecycle of the spawned backend server.
*   **Entry Point (`index.tsx`):**
    *   Serves as the main entry point for the React application, patching global API fetch. It's part of the overall structure but not directly involved in the desktop abilities themselves.
*   **PowerShell Scripts (`agent_hud.ps1`, `glow.ps1`):**
    *   `agent_hud.ps1` is empty and currently unused.
    *   `glow.ps1` creates a pulsing visual border on the screen, likely a visual cue for when the agent is active or performing desktop actions. This enhances user experience but is not a core functional ability.
*   **Inferred Missing Piece:** The actual low-level implementation for controlling the operating system (mouse, keyboard, launching apps, clipboard access) and browser automation (via Playwright) resides within the `server.ts` file or other associated backend logic that is spawned by `electron-main.js`. This is the most critical area for development to realize the outlined desktop capabilities. The `dyse_skill` directory is also a likely candidate for hosting specific agent skills/modules.

## Plan for Enhancement and Full Enablement

The objective is to fully realize and integrate the described desktop control capabilities ("mouse, keyboard, open apps, run shell commands, use clipboard") and to establish robust communication between the Electron frontend and the backend desktop agent.

### Phase 1: Backend Implementation & Core Desktop Services (Focus: `server.ts` and Native OS Interaction)

1.  **Implement `server.ts` Desktop API Endpoints:**
    *   **Objective:** Develop or complete the `server.ts` (or an equivalent backend service, potentially in Python or another language) to expose robust API endpoints that `App.tsx` can call for low-level desktop interactions.
    *   **Details:**
        *   **Native Automation Library:** Choose and integrate a suitable cross-platform (or OS-specific, if necessary) desktop automation library.
            *   **Node.js Option:** `robotjs` (for mouse/keyboard), `child_process` (for launching apps/commands), `clipboardy` (for clipboard).
            *   **Python Option:** `pyautogui` (for mouse/keyboard/screenshot), `subprocess` (for launching apps/commands), `pyperclip` (for clipboard). If Python is chosen, `electron-main.js` would need to spawn a Python server instead of `server.ts`.
        *   **Mouse/Keyboard Control Endpoints:**
            *   `/api/system/action/click`: `POST { x: number, y: number, button?: 'left'|'right' }`
            *   `/api/system/action/type`: `POST { text: string }` (simulates typing)
            *   `/api/system/action/press_key`: `POST { key: string, modifiers?: string[] }`
            *   `/api/system/action/scroll`: `POST { deltaX: number, deltaY: number }`
            *   `/api/system/action/move_mouse`: `POST { x: number, y: number, duration?: number }`
        *   **Application Management Endpoints:**
            *   `/api/system/action/launch_app`: `POST { appName: string, args?: string[] }` (e.g., "Notepad", "WhatsApp")
            *   `/api/system/action/run_command`: `POST { command: string, cwd?: string }` (for terminal commands, respecting user consent via `CommandConfirmationModal`).
            *   `/api/system/action/get_active_window_title`: `GET`
        *   **Clipboard Management Endpoints:**
            *   `/api/system/action/get_clipboard`: `GET` (returns clipboard content)
            *   `/api/system/action/set_clipboard`: `POST { text: string }` (sets clipboard content)
        *   **Screenshot Capability:**
            *   `/api/system/screenshot`: `GET` (returns base64 encoded screenshot of the entire desktop). This is already referenced in `App.tsx`.
        *   **Glow Control:** Implement `/api/system/glow/start` and `/api/system/glow/stop` to execute `glow.ps1` or an equivalent (e.g., Python script) for visual feedback.
2.  **Playwright Integration (if not already fully functional):**
    *   **Objective:** Ensure the backend `server.ts` can reliably control a browser using Playwright, including taking screenshots and executing complex web tasks. `App.tsx` already has calls to `/api/computer/browser-agent` and `/api/computer/action`.
    *   **Details:** The `server.ts` should host the Playwright instance, providing endpoints for navigation, element interaction (click, type, get text), and screenshot capture, making them available to `runComputerAgent` and `executeComputerAction`.

### Phase 2: Frontend Integration & Agent Tooling (Focus: `App.tsx` and Agent Logic)

1.  **Desktop Agent Orchestration (`runDesktopAgent`):**
    *   **Objective:** Enhance `runDesktopAgent` in `App.tsx` to orchestrate sequences of backend desktop actions based on the agent's reasoning.
    *   **Details:**
        *   The `runDesktopAgent` function currently calls `/api/system/desktop-agent`. This endpoint should not just return steps but should be an intelligent loop that receives a high-level task, breaks it down, calls the granular desktop API endpoints (from Phase 1), observes results (e.g., new screenshots, window titles), and iterates until the task is complete.
        *   The `DesktopAgentStep` state in `App.tsx` should accurately reflect the granular actions taken by the backend agent (e.g., "Launching Notepad", "Typing 'Hello World'", "Clicking Save").
2.  **Tool Definitions for Gemini Model:**
    *   **Objective:** Clearly define `FunctionDeclaration` objects in `App.tsx` (or an external configuration) that represent the new desktop capabilities for the Gemini model to utilize.
    *   **Details:**
        *   Introduce a high-level tool, e.g., `execute_desktop_task`, as currently hinted by `execute_ui_action`. This tool's `task` argument will be the prompt for the backend desktop agent.
        *   Potentially, introduce more specific tools for common actions if the orchestrating agent often makes the same sub-calls (e.g., `open_application`, `send_message_whatsapp`), which would map to direct calls to the backend APIs.
3.  **UI Feedback and Visualization:**
    *   **Objective:** Provide clear visual feedback to the user about the agent's desktop actions.
    *   **Details:**
        *   Utilize `setSystemScreenshot` and `setNeuralCursor` in `App.tsx` to display real-time desktop screenshots and highlight the agent's mouse movements.
        *   Update the `DesktopAgentSteps` to show the progress and status of each sub-action.
        *   `glow.ps1` should be invoked via `/api/system/glow/start` and `/api/system/glow/stop` to clearly indicate when the agent is actively controlling the desktop.
4.  **Error Handling and User Prompts:**
    *   **Objective:** Implement robust error handling and user prompts for desktop interactions.
    *   **Details:**
        *   Ensure that failures in backend desktop actions are gracefully handled and communicated to the user in the chat interface.
        *   Refine the `CommandConfirmationModal` to provide more context about the potential impact of local commands.

### Phase 3: Configuration, Permissions, and Testing

1.  **Environment Variable Management:**
    *   **Objective:** Ensure `VITE_ENABLE_DESKTOP` is correctly configured in the Electron build process to enable/disable desktop features as intended.
    *   **Details:** Document how to set this variable for development and production builds.
2.  **Operating System Permissions:**
    *   **Objective:** Identify and guide the user through granting necessary OS-level permissions for desktop automation.
    *   **Details:** For macOS, this involves "Accessibility" permissions. For Windows, it might involve UAC prompts or specific security settings. The application should detect if permissions are missing and instruct the user on how to grant them.
3.  **Cross-Platform Compatibility:**
    *   **Objective:** Ensure the chosen native automation libraries and command execution methods work across Windows, macOS, and Linux (if supported by Electron).
    *   **Details:** Test desktop agent functionality rigorously on target operating systems. If `robotjs` or `pyautogui` are used, ensure their dependencies are correctly bundled or installed.
4.  **Security Considerations:**
    *   **Objective:** Minimize potential security risks associated with desktop control.
    *   **Details:**
        *   Reinforce the `CommandConfirmationModal` for shell commands.
        *   Strictly limit the agent's capabilities to only what's necessary for its tasks.
        *   Consider sandboxing or virtual environments for executing potentially risky commands, though this adds complexity.
5.  **Documentation of `dyse_skill`:**
    *   **Objective:** Provide clear guidelines and examples for developing new desktop-related `dyse_skill` modules that leverage the new backend capabilities.
