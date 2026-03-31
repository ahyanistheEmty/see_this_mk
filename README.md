**Plan: Implementing Desktop Control in Dyse**

**Objective:** To enable Dyse to control the user's desktop environment, including managing files, setting wallpapers, and executing arbitrary desktop tasks via AI.

**Inspiration:** `Mark-XXXV` repository (e.g., `actions/desktop.py` and `main.py`).

**Core Components:**

1.  **`desktop_control` Tool Definition:**
    *   Define a new tool in Dyse's tool registry for `desktop_control`.
    *   This tool will accept parameters similar to `Mark-XXXV`:
        *   `action` (string, enum): `wallpaper`, `wallpaper_url`, `current_wallpaper`, `organize`, `clean`, `list`, `stats`, `task`.
        *   `path` (string, optional): Path to an image file for `wallpaper` action.
        *   `url` (string, optional): URL of an image for `wallpaper_url` action.
        *   `mode` (string, optional, enum: `by_type`, `by_date`): For `organize` action.
        *   `task` (string, optional): Natural language description for AI-driven actions.

2.  **Implement Core Desktop Functions:**
    *   Create a new Python module (e.g., `dyse/actions/desktop.py`).
    *   Implement dedicated functions for well-defined actions:
        *   `list_desktop(desktop_path)`: Lists files/folders on the desktop using `pathlib`.
        *   `get_desktop_stats(desktop_path)`: Provides file count, folder count, and total size using `pathlib` and `shutil`.
        *   `clean_desktop(desktop_path)`: Archives desktop items into a date-stamped folder using `pathlib` and `shutil.move`.
        *   `organize_desktop(desktop_path, mode)`: Sorts files into type-based or date-based folders using `pathlib`, `shutil.move`, and `datetime`.
        *   `set_wallpaper(image_path)`: **OS-Specific**. This will require conditional logic based on the operating system:
            *   **Windows**: Utilize `ctypes` to call `SystemParametersInfoW`.
            *   **macOS**: Use `subprocess` to run `osascript` commands.
            *   **Linux**: Use `subprocess` to interact with `gsettings` (GNOME) or other relevant desktop environment tools.
        *   `set_wallpaper_from_web(url)`: Downloads an image from a URL using `urllib.request` to a temporary file and then calls `set_wallpaper`.
        *   `get_current_wallpaper()`: (Optional for initial implementation) OS-specific function to retrieve the current wallpaper path (complex to implement universally).

3.  **Implement AI-Powered "Task" Action:**
    *   This is the most advanced feature, enabling Dyse to handle any arbitrary desktop request.
    *   **Prompt Engineering**: Develop a specific prompt for the Gemini API (e.g., `gemini-2.5-flash`) that instructs it to generate *safe* Python code for desktop automation.
        *   **Restrictions**: Explicitly forbid file deletion (`os.remove`, `shutil.rmtree`, `unlink`), subprocess calls (`subprocess.run`, `os.system`), `exec`/`eval`, and direct file writing (`open` in write mode).
        *   **Allowed Modules**: Specify allowed modules like `pyautogui`, `pathlib` (for path manipulation), `shutil` (read/copy/move only), `os.path`, `time.sleep`, `ctypes` (Windows API), `winreg` (read-only).
    *   **Code Generation**: Call the Gemini API with the user's `task` description and the engineered prompt.
    *   **Safety Check**: Implement a function (`_is_safe_code`) to statically analyze the generated Python code for any forbidden keywords or patterns before execution.
    *   **Secure Execution**: Use Python's `exec()` function within a tightly controlled scope. Pass a dictionary of allowed global modules and built-ins to `exec()`, preventing access to sensitive system functions. Capture `print()` outputs from the executed code to be returned to the user.

4.  **Integrate into Dyse's Core Logic:**
    *   Modify Dyse's main command/tool execution loop (similar to `Mark-XXXV`'s `_execute_tool` in `main.py`).
    *   When the `desktop_control` tool is invoked:
        *   If the `action` is one of the pre-defined ones, call the corresponding Python function from `dyse/actions/desktop.py`.
        *   If the `action` is `task` or if the action is not recognized but a `task` description is provided, trigger the AI code generation, safety check, and secure execution pipeline.
        *   Return the output from the executed function or generated code to the user (and potentially speak it).

**Phased Rollout (Recommended):**

*   **Phase 2a:** Implement built-in actions (`list`, `stats`, `clean`, `organize`).
*   **Phase 2b:** Implement `wallpaper` and `wallpaper_url` (start with Windows, then add macOS/Linux).
*   **Phase 2c:** Implement the AI-powered `task` action with robust safety checks.
