num = float(input("What is your number?\n"))
div = float(input("how do you want to divide the number?\n"))
tot = int(input("How Many people are their?\n"))

divison = div / 100

totalnum = num + divison

numberper = totalnum / tot

final_amount = round(numberper, 2)

print(f"The number each person should get {final_amount}")