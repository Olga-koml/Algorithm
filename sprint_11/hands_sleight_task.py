# id 83539726
from typing import Tuple

PLAYERS = 2
LINE_NUMBERS = 4


def hands_sleight(quantity_clicks: int, combinations: str) -> int:
    result_clicks = []
    for i in combinations:
        if (
            combinations.count(i) <= quantity_clicks*PLAYERS
            and i not in result_clicks
        ):
            result_clicks.append(i)
    return len(result_clicks)


def read_input() -> Tuple[int, str]:
    quantity_clicks = int(input())
    combinations_matrix = []
    for _ in range(LINE_NUMBERS):
        combinations_matrix.append(list(map(str, input().strip().split())))
    combinations = []
    for x in combinations_matrix:
        combinations.extend(x if isinstance(x, list) else [x])
    combinations = ''.join(combinations).replace('.', '')
    return quantity_clicks, combinations


def main():
    quantity_clicks, combinations = read_input()
    print(hands_sleight(quantity_clicks, combinations))


if __name__ == '__main__':
    main()
