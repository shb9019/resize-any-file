import click
from src.compress import Compress

@click.command()
@click.argument('input_file')
@click.argument('output_file')
@click.option('--target_size', '-t', type=int)
def resize(input_file, output_file, target_size):
    Compress(input_file, output_file, target_size)


if __name__ == '__main__':
    resize()
