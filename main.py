import click
from src.compress import Compress


@click.command()
@click.argument('input_file')
@click.argument('output_file')
@click.option('--target_size', '-s', type=int)
@click.option('--preserve_dimensions', '-p', is_flag=True, default=False)
def main(input_file, output_file, target_size, preserve_dimensions):
    Compress(input_file, output_file, target_size, preserve_dimensions)
