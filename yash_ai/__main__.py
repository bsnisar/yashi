
import argparse
import asyncio

from yash_ai.console import print_terminal_command, Console
from yash_ai.generate import generate


parser = argparse.ArgumentParser(
    description="Welcome to Shai [sh + ai] - Shell Ai buddy 🤖\n\n"
                "Shai is your trusty command-line companion. Just simply express what you want your terminal to do, \n"
                "and Shai will help you with it. ",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Examples:\n"
           "  shai 'freez pip libs to requirenments.txt' # How to make requirenments.\n"
           "    pip freeze > requirements.txt \n"
           "  shai rename git branch \n"
           "    git branch -m <new-name> \n"
)
parser.add_argument('question', metavar='question', type=str, nargs='+', help='The question to my shell')

async def search(prompt):
    """Search for a query text."""
    console = Console()
    with console.status(f"thinking on how to '{prompt}'", spinner="monkey") as status:
        try:
            command = await generate(prompt)   
            print_terminal_command(command)
        except Exception as e:
           console.log(e) 


def main():
    args = parser.parse_args()
    query_text = ' '.join(args.question)
    asyncio.run(search(query_text))  

if __name__ == '__main__':
    main()