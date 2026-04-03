# Repository: dyse
**Description:** It's an AI agent driven platform for all your simple tasks to all the complex ones
**Languages:** CSS, HTML, JavaScript, PowerShell, Python, TypeScript

## README

# dyse | Desktop AI Assistant

A clean, modern AI assistant with a focus on simplicity and performance, powered by Gemini 2.5 Flash.

## How to Run Locally

### 1. Prerequisites
- **Node.js** (v18 or later)
- **Python** (optional, for the launcher)

### 2. Setup
1.  Clone or download this project.
2.  Open a terminal in the project folder.
3.  Run `npm install` to install dependencies.
4.  Create a `.env` file based on `.env.example` and add your Gemini API key (if not using the platform's key).

### 3. Launching as a Desktop App
You have two options:

#### Option A: Using Python (Recommended for beginners)
Run the launcher script:
```bash
python run_app.py
```

#### Option B: Using npm
Run the electron development command:
```bash
npm run electron:dev
```

### 4. Building for Windows (.exe)
To create a standalone installer for Windows:
```bash
npm run electron:build
```
### 5. Computer Use (Web Agent)
The "Computer Use" module uses **Playwright** to control a browser. To use this feature locally, you must install the Playwright browsers:
```bash
npx playwright install chromium
```

- **AI Core**: Real-time voice and text interaction.
- **Computer Use**: Control a web browser via AI.
- **Code Forge**: Integrated code editor and visualizer.
- **File Nexus**: Manage and analyze local files.
- **Cubing Hub**: Track and analyze Rubik's cube solves.
- **Graph Calc**: Advanced mathematical graphing.

**ITS YOWWW BOII EMTYYYY**