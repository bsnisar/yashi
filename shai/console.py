

from rich import print, pretty
from rich.console import Console
from rich.text import Text
from rich.syntax import Syntax


def print_nice_text(terminal_command: str):
    console = Console()

    suggestion = Text("SUGGESTION", "bold")
    console.print(suggestion)

    code_block = Syntax(
        terminal_command, 
        "shell", 
        #theme="colorful",
    )

    # Convert the Syntax object to a plain Text object
    text_object = Text()
    text_object.append("\n\t".join(code_block.lines))
    # Optionally, you can add further styling to the Text object
    text_object.stylize("italic", 0, len(text_object.plain))
    console.print(text_object)
