from calculator import Calculator

op = int(input('Enter the operation\n1.Addition\n'))
num1, num2 = list(map(int, input('Enter two numbers: ').split(',')))

print(Calculator.addition(num1, num2))
