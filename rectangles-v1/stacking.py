from calendar import c
from typing import List

from numpy import Infinity

from classes import PlacedSquare, Point, Square, StackingState


def get_placement_points(state: StackingState) -> List[Point]:
    squares = state.placed_squares
    placement_points = [Point(x=0, y=0)]
    for square in squares:
        top_right = Point(
            x=square.x + square.width,
            y=square.y,
        )
        placement_points.append(top_right)
        bottom_left = Point(
            x=square.x,
            y=square.y + square.height,
        )
        placement_points.append(bottom_left)

    open_placement_points = []
    for point in placement_points:
        if any(iter([square.contains(point) for square in squares])):
            continue
        open_placement_points.append(point)
    return open_placement_points


def stack(surface: PlacedSquare, squares: List[Square]) -> List[StackingState]:
    initial_state = StackingState(
        surface=surface,
        placed_squares=[],
        remaining_squares=squares,
    )
    open_states = [initial_state]
    solved_states: List[StackingState] = []
    index = 0
    while len(open_states) > 0 and index < Infinity:
        open_state = open_states.pop(0)
        square_to_place = open_state.remaining_squares.pop(0)
        placement_points = get_placement_points(open_state)
        for placement_point in placement_points:
            square_to_place_bottom_right = Point(
                x=placement_point.x + square_to_place.width,
                y=placement_point.y + square_to_place.height,
            )
            if not surface.contains(square_to_place_bottom_right):
                continue
            new_state = StackingState(
                surface=surface,
                placed_squares=[
                    *open_state.placed_squares,
                    PlacedSquare(
                        square=square_to_place,
                        point=placement_point,
                    ),
                ],
                remaining_squares=[*open_state.remaining_squares],
            )
            print("-" * surface.width)
            print(new_state)
            if len(new_state.remaining_squares) == 0:
                solved_states.append(new_state)
            else:
                open_states.append(new_state)
        index += 1

    print("len(open_states):", len(open_states))
    print("len(solved_states):", len(solved_states))
    return solved_states
