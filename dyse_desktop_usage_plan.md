### Dyse Agent: Plan for Desktop Usage Abilities

#### 1. Current State Overview

The `dyse` application, primarily through `App.tsx` and `electron-main.js`, already has a foundational architecture for desktop integration, primarily aimed at a "Neural Browser" (Computer Use) and a "Desktop Agent."

*   **`App.tsx` (Frontend - React/TypeScript)**:
    *   Manages UI state related to desktop agent activities (`desktopAgentSteps`, `isDesktopAgentRunning`, `systemScreenshot`, `computerScreenshot`, `neuralCursor`, etc.).
    *   Initiates backend API calls for desktop actions (`/api/system/desktop-agent`, `/api/computer/action`, `/api/system/action`, `/api/computer/init`, `/api/computer/close`, `/api/computer/sync-google`).
    *   Includes a comprehensive "DESKTOP AGENT" directive within the AI's `systemInstruction`, outlining desired capabilities such as controlling mouse, keyboard, opening apps, running shell commands, clipboard access, and unified agent loops.
    *   Utilizes conditional rendering based on `ENABLE_DESKTOP` environment variable, confirming the intention for Electron-specific desktop features.
    *   Integrates `glow.ps1` for visual feedback (screen border glow) when the desktop agent is active.
*   **`electron-main.js` (Electron Main Process)**:
    *   Responsible for creating the Electron `BrowserWindow` and loading the frontend.
    *   Crucially, it **spawns a child process** to run a local backend server (presumably `server.ts` or `server.js`). This server is the gateway for native desktop interactions.
    *   Demonstrates capability to execute external scripts (`glow.ps1`) and manage child processes.
*   **`glow.ps1` (PowerShell Script)**:
    *   Provides a visual "glow" border around the screen, indicating agent activity. This script is functional and integrated.
*   **`agent_hud.ps1`**: 
    *   Currently an empty file, indicating a planned but unimplemented feature for an agent Head-Up Display.

#### 2. Goal: Full Desktop Usage Abilities

To achieve "desktop usage abilities" as defined by the `App.tsx`'s AI system instruction: "It can control the mouse, keyboard, open apps, run shell commands, use the clipboard, AND use the Playwright browser — all in one unified agent loop."

This requires a robust backend capable of interacting directly with the operating system and installed applications, coupled with intelligent orchestration from the AI and clear feedback on the frontend.

#### 3. Core Components for Desktop Control & Implementation Plan

The primary area for development will be the backend server (`server.ts`) which is currently spawned by `electron-main.js`.

##### A. `server.ts` (Backend Agent Logic - **Key Development Area**)

This Node.js/TypeScript server will expose the `/api/system/*` and `/api/computer/*` endpoints and perform the actual desktop interactions.

**Proposed Structure & Functionality:**

1.  **Desktop UI Automation Module (`@dyse/desktop-automation`)**:
    *   **Purpose**: To programmatically interact with native desktop applications.
    *   **Libraries**: 
        *   **For Windows**: Potentially use Node.js wrappers around `.NET` (e.g., `edge-js` if C# is used for automation) or directly execute PowerShell/Python scripts leveraging `UIAutomation` (for Windows UI). Consider `robotjs` for basic mouse/keyboard control if applicable.
        *   **Cross-Platform (consideration)**: Libraries like `Nut.js` or `robotjs` offer basic cross-platform control but may lack deep UI introspection. More robust solutions often involve platform-specific bindings.
    *   **Core Functions to Expose via API Endpoints**:
        *   `POST /api/system/action`: General desktop action endpoint.
            *   **`action: 'openApp', args: { appName: string }`**: Launch an application (e.g., "WhatsApp", "Notepad").
            *   **`action: 'closeApp', args: { appName: string }`**: Close an application.
            *   **`action: 'typeText', args: { text: string, target?: string }`**: Simulate keyboard input.
            *   **`action: 'click', args: { x: number, y: number, button?: 'left' | 'right' }`**: Simulate mouse clicks at screen coordinates.
            *   **`action: 'findAndClick', args: { imagePath: string | base64, confidence?: number, clickOffset?: {x:number, y:number} }`**: (Advanced - Requires image recognition) Locate an element on screen via image matching and click it.
            *   **`action: 'scroll', args: { direction: 'up' | 'down' | 'left' | 'right', amount?: number, target?: string }`**: Simulate scroll actions.
            *   **`action: 'copyToClipboard', args: { text: string }`**: Place text on the system clipboard.
            *   **`action: 'pasteFromClipboard'`**: Retrieve text from the system clipboard.
            *   **`action: 'runShellCommand', args: { command: string, elevated?: boolean }`**: Execute arbitrary shell commands (with user confirmation if `elevated`). This is already present in `App.tsx` as `run_local_command`.
            *   **`action: 'getWindowTitle'`**: Get the title of the active window.
            *   **`action: 'getWindowContent'`**: (Advanced) Attempt to read text content or structure from the active window.
        *   `POST /api/system/screenshot`:
            *   **Purpose**: Capture a screenshot of the entire desktop or a specific application window.
            *   **Implementation**: Use a native library or command-line tool (e.g., `screencapture` on macOS, `scrot` on Linux, PowerShell `Get-Screenshot` or `Print-Screen` equivalents on Windows).
            *   **Output**: Return base64 encoded image data.
        *   `POST /api/system/desktop-agent`: Orchestrates complex desktop workflows.
            *   This endpoint will receive a high-level `task` and `instructions` from `App.tsx`.
            *   It will integrate with the AI model (locally or via another API call) to break down the task into a sequence of low-level desktop actions (open app, type, click, screenshot, etc.).
            *   **AI Model**: The AI model (Gemini) will be provided with the available desktop tools and a continuous visual context (screenshots) to decide the next action. This implies running the AI with vision capabilities on the backend.
            *   **Feedback**: Continuously send `desktopAgentSteps` (progress, current action, status) back to the frontend.

2.  **Browser Automation Module (`@dyse/browser-automation`)**:
    *   **Purpose**: Control a headless or headful browser (e.g., for web scraping, complex web tasks). `App.tsx` already uses `/api/computer/state`, `/api/computer/action`, `/api/computer/init`, `/api/computer/close`.
    *   **Libraries**: **Playwright** is explicitly mentioned in the `README.md` for "Computer Use (Web Agent)" and implicitly used in `App.tsx`'s `executeComputerAction`. This is a good choice.
    *   **Core Functions to Expose**:
        *   `POST /api/computer/init`: Initialize a browser instance (launch Playwright).
        *   `POST /api/computer/close`: Close the browser instance.
        *   `GET /api/computer/state`: Get current browser state (URL, screenshot, resolution).
        *   `POST /api/computer/action`: Perform browser actions.
            *   **`action: 'navigate', args: { url: string }`**: Go to a URL.
            *   **`action: 'click', args: { selector: string | {x: number, y: number} }`**: Click an element (by CSS selector or coordinates).
            *   **`action: 'type', args: { selector: string, text: string }`**: Type text into an input field.
            *   **`action: 'screenshot'`**: Capture a screenshot of the browser viewport.
            *   **`action: 'extractText', args: { selector?: string }`**: Extract text content from the page or a specific element.
            *   **`action: 'executeScript', args: { script: string }`**: Execute arbitrary JavaScript in the browser context.
        *   `POST /api/computer/sync-google`: Potentially for syncing Google login state from the Electron app to the Playwright browser context, as inferred from `App.tsx`.

3.  **Inter-Process Communication (IPC)**:
    *   The existing `fetch` calls from `App.tsx` to `/api/...` endpoints are suitable.
    *   For real-time updates from the backend agent (e.g., `desktopAgentSteps`, `systemScreenshot`), consider using WebSockets or Server-Sent Events (SSE) from `server.ts` to `App.tsx`. This would provide a more responsive user experience for agent activity.

##### B. `App.tsx` (Frontend Integration - UI/UX)

1.  **Desktop Agent Visualization**:
    *   The `desktopAgentSteps` state should be rendered in an intuitive way, showing the sequence of actions the agent is performing (e.g., "Opening Notepad...", "Typing 'Hello World'...", "Capturing Screenshot...").
    *   The `systemScreenshot` should be prominently displayed when the desktop agent is active, providing the user with real-time visual context of the agent's actions on their desktop.
    *   Enhance `neuralCursor` to accurately reflect mouse movements.
2.  **User Confirmation/Security**:
    *   The `CommandConfirmationModal` for `run_local_command` is a good model. Extend this for other impactful desktop actions (e.g., "Allow Dyse to open application 'X'?", "Allow Dyse to click at X,Y?"). This is crucial for user trust and security.
    *   Add clear indicators when the agent is in control of the desktop.
3.  **Settings**:
    *   Ensure "Desktop Agent Enabled" toggle in `PersonalitySettings` (and `SettingsModal`) correctly reflects and controls the backend agent's operation.
    *   Add settings for `desktopApiKey` and `desktopModel` as seen in `runDesktopAgent`'s API call.
4.  **`execute_ui_action` Enhancements**:
    *   Ensure the AI's directives for `EXECUTE_DESKTOP_TASK` are fully supported by the backend tools. The parsing logic already exists, but the backend must deliver.

##### C. `electron-main.js` (Electron Process Management)

1.  **Robust Server Launch & Management**:
    *   Ensure `server.ts` is launched reliably and its output is logged for debugging.
    *   Implement graceful shutdown for `serverProcess` when the Electron app quits.
    *   Consider packaging the `server.ts` process correctly in production builds to ensure it runs correctly alongside the Electron app.

##### D. `agent_hud.ps1` (Optional - Visual Feedback)

1.  **Implement Agent HUD**:
    *   **Purpose**: Provide a non-intrusive, always-on-top display of the agent's status or current objective directly on the user's desktop, separate from the main Dyse window.
    *   **Functionality**:
        *   Display current task/objective from the desktop agent.
        *   Show a subtle visual cue (e.g., pulsating icon, text overlay) indicating "Agent Active."
        *   Potentially allow simple user interaction with the HUD (e.g., "Pause Agent," "Cancel Task").
    *   This would complement the `glow.ps1` border with more informative content.

#### 4. AI Model Integration (Using Tools Effectively)

The existing `getSystemInstruction` already provides a good foundation for guiding the AI. With the backend implementation, the AI can be instructed to:

*   **Decompose Complex Tasks**: Break down user requests like "Find a recipe for lasagna and send it to John on WhatsApp" into a sequence of browser (search for recipe), desktop (open WhatsApp, type, send), and possibly API (if contacts are integrated) actions.
*   **Utilize Visual Context**: Leverage desktop screenshots (potentially processed with an external vision model or locally within `server.ts`) to understand the current UI state of native applications.
*   **Adapt to Dynamic Environments**: Re-evaluate and adjust its plan based on the actual state of the desktop environment.

#### 5. Key Changes and Implementation Details

*   **Backend Framework**: Use a lightweight Node.js framework (e.g., Express.js) within `server.ts` to manage API endpoints.
*   **Desktop Automation Libraries**:
    *   **Web Browser**: Continue using `Playwright` for browser automation.
    *   **Native UI Automation**: Research and integrate a robust Node.js library for native UI automation (e.g., `robotjs` for mouse/keyboard, or platform-specific libraries wrapped in Node.js for deeper UI inspection). For Windows, `ActiveX` objects or PowerShell cmdlets could be invoked from Node.js.
*   **Screenshot Capture**: Integrate a reliable, fast screenshot utility.
*   **Permissions**: Ensure the Electron app and the spawned `server.ts` have necessary operating system permissions for screen capture, input control, and application launching. Electron's `app.requestSingleInstanceLock()` can ensure only one instance runs.
*   **Error Handling**: Implement comprehensive error handling and reporting from `server.ts` back to `App.tsx` for robust operation.
*   **Security**: Since the agent will have significant system control, consider:
    *   **User Confirmation**: Mandatory prompts for sensitive actions (e.g., running shell commands, controlling certain applications).
    *   **Sandboxing/Isolation**: While Electron itself provides some isolation, careful consideration is needed for the spawned backend process.
    *   **Whitelisting**: Allow users to whitelist applications or commands the agent can interact with.

#### 6. Next Steps

1.  **Implement `server.ts`**: Develop the core backend logic for desktop UI automation, system interaction, and screenshot capture.
2.  **Integrate with `App.tsx`**: Connect the new backend capabilities to the existing `runDesktopAgent`, `executeSystemAction`, and `executeComputerAction` functions.
3.  **Enhance UI Feedback**: Develop the visual elements in `App.tsx` to clearly show agent activity, screenshots, and progress.
4.  **Implement `agent_hud.ps1`**: Create a simple agent HUD for on-screen status.
5.  **Test Thoroughly**: Rigorous testing across various desktop applications and scenarios will be critical.

This plan provides a roadmap to transform Dyse into a powerful desktop AI assistant.