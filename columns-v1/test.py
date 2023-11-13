import os
import random

from classes import Square, SquareWithVariants
from stacking import get_all_possible_columns, group_columns_by_height, get_column_pairs

random.seed(0)

SURFACE_WIDTH = 5
SURFACE_HEIGHT = 100
surface = Square(height=SURFACE_HEIGHT, width=SURFACE_WIDTH, id="Page #0")

SURFACE_AREA = SURFACE_WIDTH * SURFACE_HEIGHT
SQUARE_SURFACE_AREAS = [
    SURFACE_AREA * 70 / 100,
    SURFACE_AREA * 67 / 100,
    SURFACE_AREA * 63 / 100,
    SURFACE_AREA * 39 / 100,
    SURFACE_AREA * 32 / 100,
    SURFACE_AREA * 29 / 100,
    SURFACE_AREA * 27 / 100,
    SURFACE_AREA * 25 / 100,
    SURFACE_AREA * 23 / 100,
    SURFACE_AREA * 21 / 100,
    SURFACE_AREA * 19 / 100,
    SURFACE_AREA * 17 / 100,
    SURFACE_AREA * 15 / 100,
    SURFACE_AREA * 13 / 100,
    SURFACE_AREA * 11 / 100,
    SURFACE_AREA * 9 / 100,
    SURFACE_AREA * 7 / 100,
    SURFACE_AREA * 5 / 100,
    SURFACE_AREA * 3 / 100,
    SURFACE_AREA * 1 / 100,
]

SQUARE_SURFACE_AREAS = [round(surface_area, 0) for surface_area in SQUARE_SURFACE_AREAS]
total_surface_area = sum(SQUARE_SURFACE_AREAS)
print('total_surface_area:', total_surface_area)
print('SURFACE_AREA:', SURFACE_AREA)
print()

squares = [
    SquareWithVariants(squares=[Square(height=round(surface_area/columns), width=columns, id=f"Square #{square_index}") for columns in range(1,6)])
    for square_index ,surface_area in enumerate(SQUARE_SURFACE_AREAS)
]

all_possible_columns = get_all_possible_columns(squares_with_variants=squares)
print('len(all_possible_columns):', len(all_possible_columns))
stats_example = {
    "min_height": os.sys.maxsize,
    "max_height": 0,
    "average_height": 0,
    "total_height": 0,
    "amount_of_columns": 0,
}
stats_per_column_width = {}
for i in range(1, 6):
    stats_per_column_width[i] = stats_example.copy()

for column in all_possible_columns:
    width = column.width
    stats_per_column_width[width]["amount_of_columns"] += 1
    stats_per_column_width[width]["total_height"] += column.height
    if column.height < stats_per_column_width[width]["min_height"]:
        stats_per_column_width[width]["min_height"] = column.height
    if column.height > stats_per_column_width[width]["max_height"]:
        stats_per_column_width[width]["max_height"] = column.height

for column_width, stats in stats_per_column_width.items():
    if stats["amount_of_columns"] > 0:
        stats["average_height"] = round(stats["total_height"] / stats["amount_of_columns"])

for column_width, stats in stats_per_column_width.items():
    print(f"column_width: {column_width}")
    print(f"amount_of_columns: {stats['amount_of_columns']}")
    print(f"min_height: {stats['min_height']}")
    print(f"max_height: {stats['max_height']}")
    print(f"average_height: {stats['average_height']}")
    print(f"total_height: {stats['total_height']}")
    print()


print('squares[0][0]:', squares[0].get(1).height, squares[0].get(1).width)
print('squares[0][0]:', squares[0].get(2).height, squares[0].get(2).width)
print('squares[0][0]:', squares[0].get(3).height, squares[0].get(3).width)
print('squares[0][0]:', squares[0].get(4).height, squares[0].get(4).width)
print('squares[0][0]:', squares[0].get(5).height, squares[0].get(5).width)

different_heights = set()
for column in all_possible_columns:
    different_heights.add(column.height)
print('different_heights:', different_heights)
print('len(different_heights):', len(different_heights))

columns_per_height = group_columns_by_height(all_possible_columns=all_possible_columns)

column_pairs = get_column_pairs(columns_per_height=columns_per_height, pair_size=2)
print('len column_pairs:', len(column_pairs))

def inspect(column_pair):
    print('column_pair:', column_pair)
    for column in column_pair:
        print('column:', column)
        for square in column.squares:
            print('square:', square.id, square.height, square.width)

inspect(column_pairs[0])
inspect(column_pairs[1])
