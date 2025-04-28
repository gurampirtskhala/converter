def convert(ops, value):
    if ops == "km":
        return f"Metre: {value * 1000}"
    elif ops == "m":
        return f"KM: {value / 1000}"
    else:
        return "ERROR"
    
print("Hello!\n")
ops = input("KM or M? ")
value = int(input("value: "))

print(convert(ops, value))

print("\nGood bye!")
