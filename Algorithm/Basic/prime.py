# 入力値が素数か判定
import input_integer


def print_is_prime(n: int) -> None:
    for i in range(2, n):
        if n % i == 0:
            print(f'{n}は素数ではありません。')
            return

    print(f'{n}は素数です。')


def main():
    n = input_integer.get_integer_input()
    print_is_prime(n)


if __name__ == '__main__':
    main()
