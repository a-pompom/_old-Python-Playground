def get_integer_input():
    # 整数値の入力を得る
    while True:
        n = input('input integer: ')

        if n.isnumeric():
            return int(n)
        
        print(f'{n} is not a integer...')