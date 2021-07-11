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