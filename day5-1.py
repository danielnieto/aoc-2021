from typing import List
from dataclasses import dataclass
import re

input_pattern = re.compile("^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)$")


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.points: List[Point] = self._compute_points()

    def _compute_points(self) -> List[Point]:
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)

        x_start = min(self.x1, self.x2)
        x_end = max(self.x1, self.x2)
        y_start = min(self.y1, self.y2)
        y_end = max(self.y1, self.y2)

        if dx == 0:
            return [Point(x_start, y) for y in range(y_start, y_end + 1)]
        elif dy == 0:
            return [Point(x, y_start) for x in range(x_start, x_end + 1)]
        else:
            raise ValueError("Line not horizontal or vertical")


def parse_input() -> List[Line]:
    lines: List[Line] = []

    with open("day5-1-input.txt") as file:
        for file_line in file:
            x1, y1, x2, y2 = [int(n) for n in input_pattern.match(file_line).groups()]

            if x1 == x2 or y1 == y2:
                lines.append(Line(x1, y1, x2, y2))

    return lines


def main():
    lines = parse_input()

    counter = dict()

    for line in lines:
        for point in line.points:
            if point in counter:
                counter[point] += 1
            else:
                counter[point] = 1

    points = 0

    for times in counter.values():
        if times > 1:
            points += 1

    print(points)


if __name__ == "__main__":
    main()
