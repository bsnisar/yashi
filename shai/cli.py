import argparse
import asyncio

import sys

from prompt import Prompter
from console import print_nice_text


async def search(prompt):
    """Search for a query text."""
    # Perform a search using the query text
    print(f"Searching with query: {prompt}")

    prompter = Prompter('Jo6FfUghiiiG9i0xDAfuLCR8JIindK4t2HysPpfr')

    command = await prompter.generate(prompt)
    print_nice_text(command)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AI helper to a shell')
    parser.add_argument('question', metavar='question', type=str, nargs='+', help='The question to my shell')

    args = parser.parse_args()
    query_text = ' '.join(args.question)
    asyncio.run(search(query_text))