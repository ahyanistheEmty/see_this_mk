from .base_tool import BaseTool
import os
from typing import List, Optional

class FileManagementTool(BaseTool):
    """
    A tool for managing files on the local file system (read, write, list).
    """
    def __init__(self, base_path: str = "./agent_working_dir"):
        super().__init__(
            name="file_manager",
            description="Manages files and directories. Provides functions to read, write, and list files. "
                        "Ensure 'path' arguments are relative to the agent's working directory."
        )
        self.base_path = os.path.abspath(base_path)
        os.makedirs(self.base_path, exist_ok=True)
        print(f"FileManagementTool initialized. Base path: {self.base_path}")

    def _get_full_path(self, relative_path: str) -> str:
        """Helper to get the full, absolute path within the agent's working directory."""
        full_path = os.path.abspath(os.path.join(self.base_path, relative_path))
        if not full_path.startswith(self.base_path):
            raise ValueError("Attempted to access path outside of agent's working directory.")
        return full_path

    def read_file(self, path: str) -> str:
        """
        Reads the content of a specified file.

        Args:
            path: The relative path to the file to read.

        Returns:
            The content of the file as a string.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the path is outside the allowed base directory.
        """
        full_path = self._get_full_path(path)
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            raise FileNotFoundError(f"File not found or is not a file: {path}")
        with open(full_path, 'r') as f:
            content = f.read()
        print(f"Read content from {path}")
        return content

    def write_file(self, path: str, content: str) -> str:
        """
        Writes content to a specified file, creating it if it doesn't exist, or overwriting it.

        Args:
            path: The relative path to the file to write to.
            content: The string content to write.

        Returns:
            A confirmation message.

        Raises:
            ValueError: If the path is outside the allowed base directory.
        """
        full_path = self._get_full_path(path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"Wrote content to {path}")
        return f"Successfully wrote to {path}"

    def list_directory(self, path: str = ".") -> List[str]:
        """
        Lists the contents of a specified directory.

        Args:
            path: The relative path to the directory to list. Defaults to the current working directory.

        Returns:
            A list of file and directory names within the specified path.

        Raises:
            NotADirectoryError: If the path is not a directory.
            ValueError: If the path is outside the allowed base directory.
        """
        full_path = self._get_full_path(path)
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            raise NotADirectoryError(f"Directory not found or is not a directory: {path}")
        contents = os.listdir(full_path)
        print(f"Listed contents of {path}: {contents}")
        return contents

    # The 'run' method acts as a dispatcher for the file management actions
    def run(self, action: str, path: str, content: Optional[str] = None) -> Any:
        """
        Dispatches to the appropriate file management action (read, write, list).

        Args:
            action: The action to perform ('read', 'write', 'list').
            path: The relative path for the action.
            content: Required for 'write' action, the content to write.

        Returns:
            The result of the action (file content, confirmation message, or directory listing).
        """
        if action == "read":
            return self.read_file(path)
        elif action == "write":
            if content is None:
                raise ValueError("Content must be provided for 'write' action.")
            return self.write_file(path, content)
        elif action == "list":
            return self.list_directory(path)
        else:
            raise ValueError(f"Unknown action: {action}. Supported actions are 'read', 'write', 'list'.")

# Example Usage (for testing purposes, not part of the toolkit itself)
if __name__ == "__main__":
    file_tool = FileManagementTool(base_path="./temp_agent_files")

    # Clean up any previous temp files
    import shutil
    if os.path.exists("./temp_agent_files"):
        shutil.rmtree("./temp_agent_files")
    os.makedirs("./temp_agent_files", exist_ok=True)

    print("\n--- Testing File Management Tool ---")
    try:
        # Create a file
        print(file_tool.run("write", "my_document.txt", "Hello, Ahyan! This is a test document."))

        # Read the file
        print(file_tool.run("read", "my_document.txt"))

        # Create a directory and a file inside it
        print(file_tool.run("write", "subfolder/another_file.log", "Log entry 1.\nLog entry 2."))

        # List the base directory
        print(f"Root directory contents: {file_tool.run('list', '.')}")

        # List the subfolder
        print(f"Subfolder contents: {file_tool.run('list', 'subfolder')}")

        # Attempt to read a non-existent file
        try:
            file_tool.run("read", "non_existent.txt")
        except FileNotFoundError as e:
            print(f"Expected error: {e}")

        # Attempt to write outside base_path (should raise ValueError)
        try:
            file_tool.run("write", "../evil_file.txt", "Malicious content")
        except ValueError as e:
            print(f"Expected error (security): {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        if os.path.exists("./temp_agent_files"):
            shutil.rmtree("./temp_agent_files")
            print("\nCleaned up ./temp_agent_files")