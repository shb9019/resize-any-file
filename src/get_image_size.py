from io import BytesIO
from src.file_size import convert_bytes


def get_image_size(image, format, image_quality=-1):
    image_file = BytesIO()
    if image_quality != -1:
        image.save(image_file, format, optimize=True, quality=image_quality)
    else:
        image.save(image_file, format, optimize=True)
    return image_file.tell()
