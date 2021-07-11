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