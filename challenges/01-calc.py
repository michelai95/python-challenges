# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y 

print('Select operator')
print("1 .Add")
print('2 .Subtract')
print('3 .Multyiply')
print('4 .Divide')

while True:
    choice = input('Enter choice(1/2/3/4): ')

    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter 1st number: '))
        num2 = float(input('Enter second number: '))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

# https://www.programiz.com/python-programming/examples/calculator