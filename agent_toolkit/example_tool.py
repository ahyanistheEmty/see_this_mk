from .base_tool import BaseTool

class ExampleTool(BaseTool):
    def __init__(self):
        super().__init__("Example Tool", "A simple example tool that greets a name.")

    def run(self, name: str):
        return f"Hello, {name}! This is an example tool output."