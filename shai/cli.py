import argparse
import asyncio

import sys

from generate import generate
from console import print_terminal_command, Console


async def search(prompt):
    """Search for a query text."""
    console = Console()
    with console.status(f"thinking on how to '{prompt}'", spinner="monkey") as status:
        try:
            command = await generate(prompt)   
            print_terminal_command(command)
        except Exception as e:
           console.log(e) 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='shell\'s AI buddy')
    parser.add_argument('question', metavar='question', type=str, nargs='+', help='The question to my shell')

    args = parser.parse_args()
    query_text = ' '.join(args.question)
    asyncio.run(search(query_text))