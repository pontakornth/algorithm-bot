from collections import namedtuple
from PIL import Image, ImageDraw
from typing import List

SortingSpec = namedtuple("DrawSpec", "values colored_indexes color")


def get_new_image():
    """
    Get a new image and image draw object
    """
    canvas = Image.new("RGB", (480, 480), "white")
    image_draw = ImageDraw.Draw(canvas)
    return canvas, image_draw


def draw_sorting_bar(spec: SortingSpec):
    """
    Draw bar of graph according to the spec.
    Arg:
        spec (DrawSpec): Spec of image to draw
    """
    canvas, image_draw = get_new_image()
    length = len(spec.values)
    if length == 0:
        raise ValueError("Cannot draw 0 list")
    base_width = 480 / length
    for i, v in enumerate(spec.values):
        start_x = i * base_width
        start_y = 480 - v * base_width
        stop_x = start_x + base_width
        stop_y = 480
        color = spec.color if i in spec.colored_indexes else None
        image_draw.rectangle([(start_x, start_y), (stop_x, stop_y)], fill=color, outline="black", width=3)
    return canvas


def draw_queue(queue: List[SortingSpec]):
    image_sequence = []
    for spec in queue:
        image_sequence.append(draw_sorting_bar(spec))
    return image_sequence

