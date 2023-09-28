import asyncio

from rich import print, pretty
from rich.console import Console 
from rich.text import Text
from rich.syntax import Syntax
from rich.spinner import Spinner

from asyncio import Task, Event


def print_terminal_command(terminal_command: str):

    console = Console()
    console.print()
    console.print()

    suggestion = Text("SUGGESTION", "bold")
    console.print(suggestion)

    code_block = Syntax(
        terminal_command, 
        "shell", 
        #theme="colorful",
    )

    console.print(code_block)
