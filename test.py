import random

from classes import PlacedSquare, Point, Square
from stacking import stack

random.seed(0)

AMOUNT_OF_SQUARES = 10
MIN_SQUARE_WIDTH = 1
MAX_SQUARE_WIDTH = 5
MIN_SQUARE_HEIGHT = 1
MAX_SQUARE_HEIGHT = 5
SURFACE_WIDTH = 30
SURFACE_HEIGHT = 30


surface = PlacedSquare(
    square=Square(height=SURFACE_HEIGHT, width=SURFACE_WIDTH),
    point=Point(x=0, y=0),
)

print(surface)

# squares = [
#     Square(
#         width=random.randint(MIN_SQUARE_WIDTH, MAX_SQUARE_WIDTH),
#         height=random.randint(MIN_SQUARE_HEIGHT, MAX_SQUARE_HEIGHT),
#     )
#     for _ in range(AMOUNT_OF_SQUARES)
# ]


# stacked_states = stack(surface=surface, squares=squares)
