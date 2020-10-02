from io import BytesIO
from src.file_size import convert_bytes


def get_image_size(image, format):
    image_file = BytesIO()
    image.save(image_file, format, optimize=True)
    return image_file.tell()
