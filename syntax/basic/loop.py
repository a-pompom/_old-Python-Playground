# for 変数 in イテラブル:
#    処理

# 1から10までの和
sum = 0
for i in range(1, 11):
    print(i)
    sum += i

print(f"sum: {sum}")

# enumerateによるカウント・要素の出力
abcList = ['a', 'b', 'c']
for i, item in enumerate(abcList):
    print(f'index: {i}, item: {item}')