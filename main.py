from calculator import Calculator

op = int(input('Enter the operation\n1.Addition\n2.Subtraction\n3.Divide\n'))
num1, num2 = list(map(int, input('Enter two numbers: ').split(',')))

if op == 1:
    print(Calculator.addition(num1, num2))
elif op == 2:
    print(Calculator.subtraction(num1, num2))
elif op == 3:
    print(Calculator.divide(num1, num2))