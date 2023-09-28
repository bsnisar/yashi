import textwrap
import os
import platform

from cohere import AsyncClient


async def generate(prompt: str, api_key: str = os.environ.get("SHAI_COHERE_KEY")) -> str:
    if api_key is None:
        raise ValueError('env varialbe "SHAI_COHERE_KEY" is not set')
    
    async with AsyncClient(api_key) as co:  
        response = await co.generate(  
            model='command-nightly',  
            prompt = _generate_prompt(prompt),  
            max_tokens=250,  
            temperature=0.750
        )
    return response.generations[0].text
    
def _generate_prompt(prompt: str) -> str:

    # https://docs.cohere.com/docs/prompt-engineering
    task = f'''
        Create a single-line command that can be directly run in the terminal. Do not include any other text.
        The command should do what is specified in the prompt. 
        The prompt is: {prompt}
        Reply with the single line command:
    '''.format(prompt)
    res = textwrap.dedent(task)
    return res


