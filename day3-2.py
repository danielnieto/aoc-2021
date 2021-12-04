from enum import Enum, auto
from typing import List, Dict

bits = []

class Rating(Enum):
    OXYGEN = auto()
    CO2 = auto()

with open("day3-input.txt") as lines:
    for line in lines:
        bits.append([int(c) for c in line.strip()])


def count_values_at_column(arr: List[List[int]], x: int) -> Dict[int, int]:
    counter = {0: 0, 1: 0}
    for row in arr:
        counter[row[x]] += 1

    return counter


def get_most_common_value(counter: Dict[int, int]) -> int:
    return max(counter, key=counter.get)


def get_least_common_value(counter: Dict[int, int]) -> int:
    return min(counter, key=counter.get)


def are_equally_common(counter: Dict[int, int]) -> bool:
    return counter[0] == counter[1]

RATING_OPS = {Rating.OXYGEN: get_most_common_value, Rating.CO2: get_least_common_value}
VALUES_TO_KEEP = {Rating.OXYGEN: 1, Rating.CO2: 0}

def get_rating(rating: Rating, readings: List[List[int]]) -> str:
    arr = readings.copy()
    pos = 0

    while len(arr) > 1:
        counter = count_values_at_column(arr, pos)

        if are_equally_common(counter):
            value_to_keep = VALUES_TO_KEEP[rating]
        else:
            value_to_keep = RATING_OPS[rating](counter)

        arr = list(filter(lambda x: x[pos] == value_to_keep, arr))
        pos += 1

    return "".join([str(c) for c in arr[0]])

oxygen_int = int(get_rating(Rating.OXYGEN, bits), base=2)
co2_int = int(get_rating(Rating.CO2, bits), base=2)

print(co2_int * oxygen_int)
