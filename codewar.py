
def pascal_triangle():
    number = int(input("Enter a number: "))
    for i in range(1, number + 1):
        return i if number % i == 0 else 0
