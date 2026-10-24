base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

if base == 0 and exponent < 0:
    print("Zero cannot have a negative exponent.")
else:
    result = base ** exponent
    print("Result:", result)