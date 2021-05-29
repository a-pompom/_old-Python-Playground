# nの階乗を求めたい
# forループ/再帰それぞれで記述
import input_integer


def get_factorial_recursive(n: int) -> int:
    if n == 0:
        return 1

    return n * get_factorial_recursive(n - 1)


def print_factorial_for_loop(n: int) -> None:
    factorial_result = 1

    for i in range(1, n + 1):
        factorial_result = factorial_result * i

    print(f'{n}の階乗は、{factorial_result}です。')


def main():
    n = input_integer.get_integer_input()
    print_factorial_for_loop(n)
    print(f'{n}の階乗は、{get_factorial_recursive(n)}です。')


if __name__ == '__main__':
    main()
