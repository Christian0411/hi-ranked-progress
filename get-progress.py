import sys
from PIL import Image
from utils.types import Point, Color
from utils.constants import NO_EXPERIENCE_COLOR, EXPERIENCE_COLOR, PROGRESS_BAR_START, PROGRESS_BAR_END


def load_rgb_image(image_path: str) -> Image:
    try:
        im = Image.open(image_path)
        rgb_im = im.convert('RGB')
    except FileNotFoundError:
        print(f"Could not find image: {image_path}")
        exit(1)

    return rgb_im


def find_progress_end(image: Image) -> Point:
    find_point: Point = PROGRESS_BAR_START
    color_at_find_point: Color = image.getpixel(find_point)

    while(color_at_find_point != NO_EXPERIENCE_COLOR and color_at_find_point == EXPERIENCE_COLOR):
        find_point = Point(find_point.x + 1, find_point.y)
        color_at_find_point = image.getpixel(find_point)

    return Point(find_point.x - 1, find_point.y)


def calculate_progress_complete(progress_end: Point) -> float:
    return (progress_end.x - PROGRESS_BAR_START.x) / \
        (PROGRESS_BAR_END.x - PROGRESS_BAR_START.x)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 get-progress.py [image_path]")
        exit(-1)

    image_path = sys.argv[1]
    screencap: Image = load_rgb_image(image_path)
    progress_end: Point = find_progress_end(screencap)
    progress_completion: float = calculate_progress_complete(progress_end)

    print("Rank progression: {0:.2%}".format(progress_completion))


if (__name__ == "__main__"):
    main()
