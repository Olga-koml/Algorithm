# id 83644604
from typing import List, Tuple


def nearest_zeros(quantity_houses: int, houses: List[int]) -> str:
    houses_list_left = [-1] * quantity_houses
    houses_list_right = [-1] * quantity_houses

    last_zero = None
    for i in range(quantity_houses):
        if houses[i] == 0:
            last_zero = i
        if last_zero is not None:
            houses_list_left[i] = i - last_zero

    last_zero = None
    for i in range(quantity_houses - 1, -1, -1):
        if houses[i] == 0:
            last_zero = i
        if last_zero is not None:
            houses_list_right[i] = last_zero - i
    result_houses = (
        [min(houses_list_left[i], houses_list_right[i])
         if houses_list_left[i] != -1 and houses_list_right[i] != -1
         else houses_list_left[i] + houses_list_right[i] + 1
         for i in range(quantity_houses)]
    )
    return result_houses


def read_input() -> Tuple[int, List[int]]:
    quantity_houses = int(input())
    houses = list(map(int, input().split()))
    return quantity_houses, houses


def main():
    quantity_houses, houses = read_input()
    print(*nearest_zeros(quantity_houses, houses))


if __name__ == '__main__':
    main()
