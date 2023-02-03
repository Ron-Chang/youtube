"""
Password Generator

args
- number: password length
- digit: including digit
- lowercase: including lowercase
- uppercase: including uppercase
- punctuation: including punctuation
- exclude: 'ioIO'
"""
import string
import re
import random
import typer


app = typer.Typer()


@app.command()
def help():
    print(__doc__)


@app.command()
def key(
    number: int = 8,
    digit: bool = True,
    lowercase: bool = True,
    uppercase: bool = True,
    punctuation: bool = False,
    exclude: str = 'ioIO',
):
    if not isinstance(number, int) or number < 1:
        raise ValueError('number not meet min len')
    if not any([digit, uppercase, lowercase, punctuation]):
        raise ValueError('one or more pattern is required')
    pattern = str()
    if digit:
        pattern = f'{pattern}{string.digits}'
    if lowercase:
        pattern = f'{pattern}{string.ascii_lowercase}'
    if uppercase:
        pattern = f'{pattern}{string.ascii_uppercase}'
    if punctuation:
        pattern = f'{pattern}{string.punctuation}'
    if exclude:
        pattern = re.sub(f'[{exclude}]', '', pattern)
    result = ''.join(random.choice(pattern) for _ in range(number))
    print(result)


if __name__ == '__main__':
    app()
