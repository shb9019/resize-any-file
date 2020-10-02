import click
from src.compress import Compress


@click.command()
@click.argument('input_file')
@click.argument('output_file')
@click.option('--target_size', '-s', type=int, help='Output image size in bytes')
@click.option('--preserve_dimensions', '-p', is_flag=True, default=False, help='Compress image by changing quality '
                                                                               'and not dimensions')
def main(input_file, output_file, target_size, preserve_dimensions):
    Compress(input_file, output_file, target_size, preserve_dimensions)
