operation = raw_input(' Choose math operation (+, -, *, /):')
print(operation)
x = int(raw_input('Enter value for x:'))
print(x)
y = int(raw_input('Enter value for y:'))
print(y)
print('Result')
# print(x+y)
# str()
# float()

if operation == '+':
    print(x+y)
elif operation == '-':
    print(x-y)
elif operation == '*':
    print(x*y)
elif operation == '/':
    print(x/y)
else:
    print('Wrong operation!')
