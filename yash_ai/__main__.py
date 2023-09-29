
import argparse
import asyncio

from yash_ai.console import print_terminal_command, Console
from yash_ai.generate import generate


parser = argparse.ArgumentParser(
    description="Welcome to Yashi - Yet Another Shell Ai Command-Line Companion, the Cat 🤖\n\n"
                " /\_/\  \n"
                "( o.o ) \n"
                "/  |  \ \n\n"
                "Yashi is your trusty command-line companion, just simply express what \n"
                "you want your terminal to do, and Yashi will help you with it.\n\n"
                "",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Examples:\n"
           "~$  yashi 'freez pip libs to requirenments.txt' \n"
           "    pip freeze > requirements.txt \n"
           "~$  yashi rename git branch \n"
           "    git branch -m <new-name> \n"
)
parser.add_argument('question', metavar='question', type=str, nargs='+', help='The question to my shell')

async def search(prompt):
    """Search for a query text."""
    console = Console()
    with console.status(f"thinking on how to '{prompt}'", spinner="dots") as status:
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