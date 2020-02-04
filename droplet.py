from asciimatics.effects import RandomNoise
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

# Draw a large with a smaller rectangle hole in the middle.
screen.fill_polygon([[(60, 0), (70, 0), (70, 10), (60, 10)],
         [(63, 2), (67, 2), (67, 8), (63, 8)]])

def demo(screen):
    effects = [
        RandomNoise(screen,
                    signal=Rainbow(screen,
                                   FigletText("ASCIIMATICS")))
    ]
    screen.play([Scene(effects, -1)], stop_on_resize=True)
    # Draw a large with a smaller rectangle hole in the middle.
    screen.fill_polygon([[(60, 0), (70, 0), (70, 10), (60, 10)],
                     [(63, 2), (67, 2), (67, 8), (63, 8)]])


while False:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass
