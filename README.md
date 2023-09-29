```shell
$ yashi
  /\_/\
 ( o.o )
 /  |  \
```

## Yashi: Yet Another SHell aI Command-Line Companion

[![PyPI version](https://badge.fury.io/py/yash-ai.svg)](https://pypi.org/project/yash-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Are you a person who had trouble remembering shell commands and flags for all shell commands? This is yet another helper that 
can make the shell more human-friendly. Just say what to do, not remember. Simply input what you want to do in natural language, and `yashi` will suggest single-line commands that achieve your intent.


![](https://raw.githubusercontent.com/bsnisar/yashi/main/assets/example.gif)

## Usage
You can install Shell-AI directly from PyPI using pip:
```
pip install yash-ai
```

After installation, you can use `yashi` cli.

## Keys

This tool based on [Cohere](https://cohere.com/) LLM service. To enable CLI working you should expose [api key](https://dashboard.cohere.com/api-keys) as env variable and enjoy.
```
export YASHI_COHERE_KEY='gYjIU2+....'
```
 
