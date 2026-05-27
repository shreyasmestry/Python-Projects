temp=int(input("Enter the temperature in celsius:"))

def celsius(temp):
    fahrenheit=(temp*1.8+32)
    return fahrenheit
print(f"Fahrenheit for {temp} is {celsius(temp)}")
print(celsius(temp))