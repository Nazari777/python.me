first = float(input("enter your first number: "))
second = float(input("enter your second number: "))
operation = input("enter a operation(+, -, *, /): ")

result = eval(f"{first} {operation} {second}")
print(result)