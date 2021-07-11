# 制御構造

## falsyなオブジェクトは何か

* None
* False
* 0
* 空のコンテナオブジェクト
* __bool__()がFalseを返すオブジェクト
* __bool__()が未定義で、__len__()が0を返すオブジェクト

## forループの種類

基本構文は、`for 変数 in イテラブル:`で表される。
イテラブルには、決まった回数を表すオブジェクトが使えると便利なので、`range(回数)`メソッドが提供されている。
また、`for count, item in enumerate(イテラブル)`構文を使えば、イテラブルの要素・ループインデックスを同時に扱うことができる。


# データ型

### None

Noneはシングルトンなので、==(`__eq__()`)ではなく、isによる厳密な比較による
等値判定が必要。

### bool型

orは最初にtrueと評価されたオブジェクト・andは右辺のオブジェクトが戻り値となる。

### 数値型

* int
* float
* complex

### 文字列型(str)

Pythonでは、文字列はイテラブルで不変なオブジェクトである。

### bytes型

`str.encode()`・`bytes.decode()`で相互変換される。

### 配列

* list
* tuple

### 辞書

* dict型 キーにはイミュータブルなオブジェクトのみ使用可能

### 内包表記

`[リストの要素 for 変数 in イテラブルなオブジェクト if 条件式]`または、
`{辞書のキー: 値 for 変数 in イテラブルなオブジェクト if 条件式}`でリストや辞書を簡潔に記述できる。


# 関数

### アンパック

タプルのアンパックは位置引数へと変換される。
そして、辞書のアンパックはキーワード引数へ変換される。

### ラムダ式

> lambda arg1, arg2, ...: return expression

の形式で記述。

<details>
<summary>サンプル</summary>

```Python
# タプルのアンパックは位置引数へ
def concat(*args) -> str:
    result = ''
    for item in args:
        result = f'{result}{item}'
    
    return result

str_tuple = ('hello', ' ', 'tuple', ' ', 'unpack')

# hello tuple unpack
print(concat(*str_tuple))


# 辞書のアンパックはキーワード引数へ
def sum(former: int, latter: int) -> int:
    return former + latter

arg_dict = {'former': 7, 'latter': 3}
# 10
print(f'7 + 3 = {sum(**arg_dict)}')

sum_lambda = lambda former, latter: former + latter
# 2
print(f'1 + 1 = {sum_lambda(1,1)}')
```

</details>

# 練習問題(fizz-buzz)

```Python
def printFizzBuzz(input: int) -> None:

    if input % 15 == 0:
        print('FizzBuzz!!')
        return

    if input % 3 == 0:
        print('Fizz')
        return

    if input % 5 == 0:
        print('Buzz')
        return

    print(f'{input}')
    return

for i in range(1, 101):
    printFizzBuzz(i)
```