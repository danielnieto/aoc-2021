from typing import List, Tuple
import re


class Board:
    def __init__(self, content: List[List[int]]):
        self.content = content
        self.marked = [[False for _ in row] for row in content]
        self.is_still_playing = True

    def mark(self, value: int) -> None:
        for i in range(len(self.content)):
            for j in range(len(self.content[i])):
                if self.content[i][j] == value:
                    self.marked[i][j] = True

    def has_won(self) -> bool:
        for row in self.marked:
            if all(row):
                return True
        for col in zip(*self.marked):
            if all(col):
                return True
        return False

    def get_sum_of_unmarked_values(self) -> int:
        sum = 0
        for i, row in enumerate(self.marked):
            for j, value in enumerate(row):
                if not value:
                    sum += self.content[i][j]
        return sum


def parse_input() -> Tuple[List[int], List[Board]]:
    boards: List[Board] = []
    board_content: List[List[int]] = []
    draws: List[int]

    with open("day4-1-input.txt") as lines:
        for i, line in enumerate(lines):
            if i <= 1:
                draws = [int(c) for c in line.strip().split(",")] if i == 0 else draws
                continue

            if line == "\n":
                boards.append(Board(board_content))
                board_content = []
            else:
                board_content.append(
                    [int(c) for c in re.sub(" +", " ", line.strip()).split(" ")]
                )

        boards.append(Board(board_content))

    return draws, boards


def main():

    draws, boards = parse_input()
    place = 0

    for draw in draws:
        for board in boards:
            if board.is_still_playing:
                board.mark(draw)
                if board.has_won():
                    board.is_still_playing = False
                    place += 1

                    if place == len(boards):
                        print(board.get_sum_of_unmarked_values() * draw)
                        return


if __name__ == "__main__":
    main()
