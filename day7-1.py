from typing import List


def parse_input() -> List[int]:
    with open("day7-1-input.txt") as file:
        return [int(c) for c in file.readline().strip().split(",")]


def main():
    positions = parse_input()
    sums = {}
    for i in range(min(positions), max(positions) + 1):
        if i in sums:
            continue

        sums[i] = sum([abs(i - pos) for pos in positions])

    print(sums[min(sums, key=sums.get)])


if __name__ == "__main__":
    main()
