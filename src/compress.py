from PIL import Image
from click import echo
from src.file_size import file_size, convert_bytes
from src.get_image_size import get_image_size


class Compress:
    def __init__(self, input_file, output_file, target_size):
        self.input_file = input_file
        self.output_file = output_file
        self.target_size = target_size

        try:
            self.input_image = self.open_input_file()
        except OSError:
            # TODO: Check all cases where this can happen.
            echo('Input file cannot be opened!')
            return

        (image_format, image_size) = self.get_input_image_details()
        if image_format not in ('JPEG', 'JPG'):
            print('Only JPGs and JPEGs are supported at the moment.')
            return

        self.print_input_image_details(image_format, image_size)

        self.resize_image(image_format, image_size)
        echo('Resized Successfully!')
        self.output_image = self.open_output_file()
        (output_format, output_size) = self.get_output_image_details()
        self.print_image_details(output_format, output_size)

    def open_input_file(self):
        return Image.open(self.input_file)

    def open_output_file(self):
        return Image.open(self.output_file)

    def get_input_image_details(self):
        return self.input_image.format, self.input_image.size

    def get_output_image_details(self):
        return self.output_image.format, self.output_image.size

    def print_input_image_details(self, image_format, image_size):
        print('Input Image:')
        echo('  Type: ' + image_format)
        echo('  Width: ' + str(image_size[0]) + 'px')
        echo('  Height: ' + str(image_size[1]) + 'px')
        self.print_input_file_size()
        echo('')

    def print_image_details(self, output_format, output_size):
        print('Output Image:')
        echo('  Type: ' + output_format)
        echo('  Width: ' + str(output_size[0]) + 'px')
        echo('  Height: ' + str(output_size[1]) + 'px')
        echo('  File Size: ' + file_size(self.output_file))
        echo('')

    def print_input_file_size(self):
        echo('  File Size: ' + file_size(self.input_file))

    def resize_image(self, image_format, image_dimensions):
        (image_width, image_height) = image_dimensions

        higher_resize_height = 10000
        lower_resize_height = 1

        while (higher_resize_height - lower_resize_height) > 1:
            resize_height = int((higher_resize_height + lower_resize_height) / 2)
            resized_width = int((image_width * resize_height) / image_height)
            resized_image = self.input_image.resize((resized_width, resize_height))
            image_size = get_image_size(resized_image, image_format)

            if image_size > self.target_size:
                higher_resize_height = resize_height - 1
            else:
                lower_resize_height = resize_height

        final_height = lower_resize_height
        final_width = int((image_width * final_height) / image_height)
        resized_image = self.input_image.resize((final_width, final_height))
        resized_image.save(self.output_file, image_format, optimize=True)

        return resized_image
