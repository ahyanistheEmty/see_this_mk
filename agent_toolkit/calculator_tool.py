from .base_tool import BaseTool
import operator

class CalculatorTool(BaseTool):
    """
    A tool for performing basic arithmetic calculations.
    """
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Performs basic arithmetic operations (addition, subtraction, multiplication, division). "
                        "Input should be an 'expression' string, e.g., '10 + 5' or '15 / 3'. "
                        "Returns the numerical result of the expression."
        )
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def run(self, expression: str) -> float:
        """
        Evaluates a simple arithmetic expression.

        Args:
            expression: A string representing a simple arithmetic expression
                        (e.g., "10 + 5", "15 / 3"). Supports +, -, *, /.

        Returns:
            The float result of the expression.

        Raises:
            ValueError: If the expression is malformed or contains unsupported operators.
            ZeroDivisionError: If division by zero occurs.
        """
        try:
            parts = expression.split()
            if len(parts) != 3:
                raise ValueError("Expression must be in the format 'operand1 operator operand2'.")

            operand1 = float(parts[0])
            op_symbol = parts[1]
            operand2 = float(parts[2])

            operation = self.operators.get(op_symbol)
            if not operation:
                raise ValueError(f"Unsupported operator: {op_symbol}. Supported are +, -, *, /.")

            result = operation(operand1, operand2)
            print(f"Calculated '{expression}' = {result}")
            return result
        except ZeroDivisionError:
            print(f"Error: Division by zero in expression '{expression}'")
            raise
        except ValueError as e:
            print(f"Error parsing expression '{expression}': {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred during calculation: {e}")
            raise

# Example Usage (for testing purposes, not part of the toolkit itself)
if __name__ == "__main__":
    calculator = CalculatorTool()
    print("\n--- Testing Calculator Tool ---")
    try:
        print(f"Result: {calculator.run('10 + 5')}")
        print(f"Result: {calculator.run('25 * 4')}")
        print(f"Result: {calculator.run('100 / 20')}")
        print(f"Result: {calculator.run('50 - 15.5')}")
        # Test error cases
        try:
            calculator.run('10 / 0')
        except ZeroDivisionError as e:
            print(f"Expected error: {e}")
        try:
            calculator.run('10 plus 5')
        except ValueError as e:
            print(f"Expected error: {e}")
        try:
            calculator.run('10 + 5 + 3')
        except ValueError as e:
            print(f"Expected error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")