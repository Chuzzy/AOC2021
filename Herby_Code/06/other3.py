from __future__ import annotations

from collections import Counter
from pathlib import Path


def cycle(pool: dict[int, int]) -> dict[int, int]:
    return {
        8: pool[0],
        7: pool[8],
        6: pool[7] + pool[0],
        5: pool[6],
        4: pool[5],
        3: pool[4],
        2: pool[3],
        1: pool[2],
        0: pool[1],
    }


def solve(days: int) -> int:
    #input_path = Path(__file__).parent / "input.txt"

    with open('6.txt') as input_file:
        line = input_file.read()

    pool = Counter([int(fish) for fish in line.strip().split(",")])

    for _ in range(days):
        pool = cycle(pool)

    return sum(val for val in pool.values())


if __name__ == "__main__":
    print(solve(256))
