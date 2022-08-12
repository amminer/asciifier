# Known bugs:
# at large terminal sizes (very zoomed out) image takes on diamond-shaped
#   rgb artifacting?
# at extreme terminal aspect ratios similar artifacting occurs as the image is
#   very slightly stretched along the long axis of the terminal window...
# lame and obfuscated behind PIL as these bugs are, this is kinda better than
#   the earlier version.
# transparency for nonRGB images turns white, should turn black (Image.convert)
# TODO
# choose ascii char based on brightness?
# output array is way way longer than it should be, but it works so?????
# could effectively increase output "pixel" density by 2x as many column
#   samples as row samples?

from PIL import Image
from sys import argv, exit
from os import get_terminal_size


def getChar(maxBrightness, brightness):
    chars = ["'", '"', "*", "!", "?", "%", "#"]
    interval = maxBrightness / len(chars)
    for charIndex in range(0, )

class outputChar:
    def __init__(self) -> None:
        self.char = None
        self.r = -1
        self.g = -1
        self.b = -1

class output:
    def __init__(self) -> None:
        self.chars = []
        
    def read(filepath=argv[1]):



def main():
    resize_method = Image.LANCZOS
    max_height = get_terminal_size().lines - 1  # -1 accounts for prompt line
    max_width = get_terminal_size().columns // 2  # //2 accounts for char width
    new_height, new_width = max_height, max_width
    img_path = argv[1]
    im = Image.open(img_path).convert("RGB")
    # reduce contrast for char selection effect?
    problem_dim = max(new_width, new_height)
    im.thumbnail((problem_dim, problem_dim), resize_method)
    while im.size[0] > max_width or im.size[1] > max_height:  # img sz > terminal
        problem_dim = max(new_width, new_height)
        im.thumbnail((problem_dim, problem_dim), resize_method)
        new_height -= 1
        new_width -= 1

    output = []
    for j in range(im.size[1]):
        for i in range(im.size[0]):  # one iteration for each char in output
            pix = im.getpixel((i, j))
            r = pix[0]
            g = pix[1]
            b = pix[2]
            brightness = r + g + b

            char = "#"  # TODO
            output += f"\033[38;2;{r};{g};{b}m{char}" * 2 + "\033[38;2;255;255;255m"
        output += "\n"  # line break at end of each row

    # print(new_width * new_height)
    # print(len(output)) # WHY??? TODO

    for c in output:
        print(c, end="")


if __name__ == "__main__":
    main()
