import json
from typing import List


class Point:
    def __init__(self, *, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return json.dumps({"x": self.x, "y": self.y}, indent=4)


class Square:
    def __init__(self, *, height: int, width: int):
        self.height = height
        self.width = width

    def __str__(self) -> str:
        return json.dumps({"width": self.width, "height": self.height}, indent=4)

    def calculate_surface_area(self):
        return self.height * self.width


class PlacedSquare:
    def __init__(self, *, square: Square, point: Point):
        self.width = square.width
        self.height = square.height
        self.x = point.x
        self.y = point.y

    def __str__(self) -> str:
        return json.dumps(
            {"width": self.width, "height": self.height, "x": self.x, "y": self.y},
            indent=4,
        )

    def calculate_surface_area(self):
        return self.height * self.width

    def contains(self, point: Point) -> bool:
        is_between_x = self.x <= point.x <= self.x + self.width - 1
        is_between_y = self.y <= point.y <= self.y + self.height - 1
        return is_between_x and is_between_y

    def borders(self, point: Point) -> bool:
        is_between_x = self.x <= point.x <= self.x + self.width - 1
        is_between_y = self.y <= point.y <= self.y + self.height - 1
        borders_x = point.x == self.x or point.x == self.x + self.width - 1
        borders_y = point.y == self.y or point.y == self.y + self.height - 1
        return (borders_x and is_between_y) or (borders_y and is_between_x)


class StackingState:
    def __init__(
        self,
        *,
        surface: PlacedSquare,
        placed_squares: List[PlacedSquare],
        remaining_squares: List[Square],
    ):
        self.surface = surface
        self.placed_squares = placed_squares
        self.remaining_squares = remaining_squares

    def __str__(self) -> str:
        columns = self.surface.width
        rows = self.surface.height
        grid = []
        squares_to_draw = [
            *self.placed_squares,
        ]
        for y in range(rows):
            row = ["."] * columns
            grid.append(row)
            for x in range(columns):
                point = Point(x=x, y=y)
                for square_index, square in enumerate(squares_to_draw):
                    if square.borders(point):
                        grid[y][x] = str(square_index)

        return "\n".join(["".join(row) for row in grid])
