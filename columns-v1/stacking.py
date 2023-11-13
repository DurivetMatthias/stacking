import itertools

from typing import List

from classes import Column ,SquareWithVariants

MAX_SQUARES_PER_COLUMN = 5

def get_all_possible_columns(*, squares_with_variants: List[SquareWithVariants]):
    columns = []
    for column_width in range(1,6):
        squares = [square.get(column_width) for square in squares_with_variants]
        for squares_per_column in range(1, MAX_SQUARES_PER_COLUMN + 1):
            combinations = itertools.combinations(squares, squares_per_column)
            columns.extend([Column(squares=combinations) for combinations in combinations])
    return columns

def group_columns_by_height(*, all_possible_columns: List[Column]):
    columns_per_height = {}
    for column in all_possible_columns:
        if column.height not in columns_per_height:
            columns_per_height[column.height] = []
        columns_per_height[column.height].append(column)
    return columns_per_height

def get_column_pairs(*, columns_per_height: dict, pair_size: int = 2):
    column_pairs = []
    for columns in columns_per_height.values():
        combinations = list(itertools.combinations(columns, pair_size))
        for combination in combinations:
            unique_squares = set()
            has_duplicate_squares = False
            if sum(column.width for column in combination) == 5:
                for column in combination:
                    for square in column.squares:
                        if square.id in unique_squares:
                            has_duplicate_squares = True
                            break
                        unique_squares.add(square.id)
                if not has_duplicate_squares:
                    column_pairs.append(combination)
    return column_pairs
