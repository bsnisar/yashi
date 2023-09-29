# pylint: disable=missing-function-docstring
# pylint: disable=broad-exception-caught
# pylint: disable=anomalous-backslash-in-string


import argparse
import asyncio

from rich_argparse import RawTextRichHelpFormatter

from yash_ai.console import print_terminal_command, status, Console
from yash_ai.generate import generate


parser = argparse.ArgumentParser(
    description="Welcome to Yashi - Yet Another Shell Ai Command-Line Companion, the Cat\n"
                "[bold cyan]  /\_/\  [/bold cyan]\n"
                "[bold cyan] ( o.o ) [/bold cyan]\n"
                "[bold cyan] /  |  \ [/bold cyan]\n\n"
                "Yashi is your trusty command-line companion, just simply express what \n"
                "you want your terminal to do, and Yashi will help you with it.\n\n"
                "",
    formatter_class=RawTextRichHelpFormatter,
    epilog="Examples:\n"
           "~$  [dark_orange]yashi[/dark_orange] 'freez pip libs to requirenments.txt' \n"
           "    pip freeze > requirements.txt \n"
           "~$  [dark_orange]yashi[/dark_orange] rename git branch \n"
           "    git branch -m <new-name> \n"
)
parser.add_argument('question', metavar='question', type=str, nargs='+',
                    help='The question to my shell')

async def search(prompt):
    """Search for a query text."""
    console = Console()
    with status():
        try:
            command = await generate(prompt)
            print_terminal_command(command)
        except Exception as ex:
            console.log(ex)


def main():
    args = parser.parse_args()
    query_text = ' '.join(args.question)
    asyncio.run(search(query_text))

if __name__ == '__main__':
    main()
