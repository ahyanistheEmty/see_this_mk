from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    """
    Abstract base class for all AI agent tools.
    All tools should inherit from this and implement the 'run' method.
    """
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args, **kwargs) -> Any:
        """
        Executes the logic of the tool.
        This method should be implemented by all concrete tool classes.
        """
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Converts the tool's essential information to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self._get_parameters_schema() # Placeholder, would parse run method signature
        }

    def _get_parameters_schema(self) -> Dict:
        """
        Placeholder method to generate a schema for the tool's parameters.
        In a real framework, this would dynamically inspect the 'run' method's signature.
        For these examples, the description will guide the LLM on parameters.
        """
        return {} # Simplified for demonstration
