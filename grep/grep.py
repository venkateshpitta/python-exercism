from typing import List, Union, Tuple
import click

Output = Union[Tuple[str], str]

@click.command()
@click.argument('word', type=click.STRING, nargs=1)
@click.argument('filenames', type=click.STRING, nargs=-1)
@click.option('-n', type=click.BOOL, is_flag=True, default=False, help='Print the line number of each matching line.')
@click.option('-i', type=click.BOOL, is_flag=True, default=False, help='Match line using a case-insensitive comparison.')
@click.option('-l', type=click.BOOL, is_flag=True, default=False, help='Print only the names of files that contain at least one matching line.')
@click.option('-x', type=click.BOOL, is_flag=True, default=False, help='Only match entire lines, instead of lines that contain a match.')
@click.option('-v', type=click.BOOL, is_flag=True, default=False, help='Only match entire lines, instead of lines that contain a match.')
def grep(word, filenames, n, i, l, x, v) -> Output:
    pass

