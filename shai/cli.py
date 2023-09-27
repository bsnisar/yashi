import click

@click.command()
@click.option('--number', '-n', type=float, prompt='Enter a number', help='The number to calculate square and cube for')
def calculate(number):
    """Calculate the square and cube of a number."""
    square = number ** 2
    cube = number ** 3
    click.echo(f"Square of {number}: {square}")
    click.echo(f"Cube of {number}: {cube}")

if __name__ == '__main__':
    calculate()