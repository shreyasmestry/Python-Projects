# number=int(input("Enter a number : "))
# # for k in range(10,1,-1):
# #     print(f"{number}*{k}={number*k}")
# i=11
# while i>=10:
#     print(number*i)
#     i=i+1
while True:
        operator = input("Enter operator (+,-,*,/) or 'quit': ").lower()
        if operator == "quit": break
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator.")
            continue
        n1, n2 = float(input("Num 1: ")), float(input("Num 2: "))
        if operator == "+": print(int(n1 + n2))
        elif operator == "-": print(n1 - n2)
        elif operator == "*": print(n1 * n2)
        elif operator == "/":
                print(n1 / n2 if n2 != 0 else "Error: Div by 0")