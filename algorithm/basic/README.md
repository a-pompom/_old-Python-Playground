# 1からnまでの和

## 目的

`input()`の使い方を復習。
アルゴリズムの肩慣らし。

### input()

[参考](https://docs.python.org/3/library/functions.html#input)

> input([prompt])

形式で記述し、戻り値は文字列。通常、改行コードは取り除かれる。

### isnumeric()

数値かどうか判定。`isdigit()`, `isdecimal()`と、やたら種類が多いが、
どうやらUnicodeあたりが絡んでいるっぽい。
[参考](https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python)

<details>
<summary>コード</summary>

```Python
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
```

</details>