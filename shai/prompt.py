import textwrap

from cohere import AsyncClient



class Prompter:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def generate(self, prompt: str) -> str:
        async with AsyncClient(self._api_key) as co:  
            response = await co.generate(  
                model='command-nightly',  
                prompt = self._generate_prompt(prompt),  
                max_tokens=250,  
                temperature=0.750
            )
            return response.generations[0].text
    

    def _generate_prompt(self, prompt: str) -> str:
        # https://docs.cohere.com/docs/prompt-engineering
        task = f'''
            Create a single line command that one can be directly run in the a terminal. Do not include any other text.
            The command should do what is specified in the prompt.
            The prompt is: {prompt}
            Reply with the single line command:
        '''.format(prompt)

        return textwrap.dedent(task)