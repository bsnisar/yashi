import random
import rich
from rich.status import Status
from rich.text import Text
from rich.syntax import Syntax

# pylint: disable=unused-import
from rich.console import Console
# pylint: enable=unused-import

phrases = [
    "Pouncing...",
    "Chasing mice...",
    "Hunting for data...",
    "Curiosity in progress...",
    "Whiskers twitching...",
    "Tail-tapping...",
    "Napping... Just kidding!",
    "Napping... Oops, no time for that!",
    "Meow-magic happening...",
    "Catnip break... Just joking!",
    "Paws at work...",
    "Purr-fecting your request...",
    "Cat-tering to your needs...",
    "Stretching, but still working...",
    "Cat-ulating results...",
    "Climbing the data tree...",
    "Snoozing... Just a quick catnap!",
    "Cat-mand executed...",
    "Paw-sitively fetching results...",
    "On the prowl for answers..."
]

def status() -> Status:
    """
    Run Status spinner with random phrase
    """

    phrase = random.choice(phrases)
    return rich.get_console().status(phrase, spinner="dots")

def print_terminal_command(terminal_command: str):
    """
    Display a formatted terminal command in the console.

    Args:
        terminal_command (str): The terminal command to be displayed.

    Example:
        >>> print_terminal_command("ls -l")
    """
    console = rich.get_console()
    suggestion = Text("Suggestions", style="bold")
    console.print("\n", suggestion, "\n")

    code_block = Syntax(terminal_command, "shell")
    console.print(code_block)
    console.print("")
