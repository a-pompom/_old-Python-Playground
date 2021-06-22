def get_integer_input():
    """
    整数値の入力を得る
    :return: 整数値
    """
    while True:
        n = input('input integer: ')

        if n.isnumeric():
            return int(n)
        
        print(f'{n} is not a integer...')