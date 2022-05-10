from PIL import Image


def find_the_message(image_path: str) -> str:
    """
    The function gets a path to the image and checks where the black pixels are in it
     and decodes the message encrypted there by the row number of the black pixels.
    :param image_path: The path of the image.
    :return: The encrypted message.
    """
    image = Image.open(image_path, 'r')
    width, height = image.size
    # Taking just the pixel of the row.
    return ''.join(map(str, [chr(j) for i in range(width) for j in range(height) if image.getpixel((i, j)) == 1]))


if __name__ == '__main__':
    path_image = input("Please insert the path of the image:\n")
    print(f"The encrypted message is:\n{find_the_message(path_image)}")
