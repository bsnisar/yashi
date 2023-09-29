from rich.console import Console
from rich.text import Text
from rich.syntax import Syntax


def print_terminal_command(terminal_command: str):
    """
    Display a formatted terminal command in the console.

    Args:
        terminal_command (str): The terminal command to be displayed.

    Example:
        >>> print_terminal_command("ls -l")
    """
    console = Console()

    suggestion = Text("Suggestions", style="bold")

    console.print("\n\n", suggestion, "\n")

    code_block = Syntax(terminal_command, "shell")
    console.print(code_block)
