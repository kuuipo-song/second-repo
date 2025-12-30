def fizz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        else:
            print(i)


def buzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)

