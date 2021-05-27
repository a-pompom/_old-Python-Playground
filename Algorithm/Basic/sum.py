# 1からnまでの和を求める

def get_sum_input():
    # 整数値の入力を得る
    while True:
        n = input('input integer: ')

        if n.isnumeric():
            return int(n)
        
        print(f'{n} is not a integer...')

def sum_by_for_loop(n: int) -> None:

    # 和の算出
    sum = 0
    for i in range(1, n+1):
        sum += i
    
    print(f'1から{n}までの和は、{sum}です。')


def main():

    print('1からnまでの和を計算します。')

    n = get_sum_input()
    sum_by_for_loop(n)


if __name__ == '__main__':
    main()