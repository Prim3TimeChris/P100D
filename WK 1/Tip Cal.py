# I really have to go back on day 2 and understand this before moving forward because this
# is confusing lol but let me break it down 

# line five is the opening 
print("welcome to the Tip Calculator")
#next few lines are inputs
# using variables for the answer the line before the input is telling the computer what strings
# / answers the person inputting is allowed to give
# and since its asking for a float you can give any number
bill = float(input("What was the total bill? $"))
# like here you can't give a decimal number because it is asking for an integer i changed this to a float
# before it was an int now i can give any number
tip = float(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill "))

# using operators to basically give the answer this second half is tough
tip_as_percent = tip / 100

# uses math here 
total_tip_amount = bill * tip_as_percent
# creates total bill variable and adds  it togther
total_bill = bill + total_tip_amount
# total bill variable is divided by people variable above
bill_per_person = total_bill / people
# uses round function to round up final answers that's also why you need the two there
final_amount = round(bill_per_person, 2)
# using print f function you do the final calculations
print(f"Each person should pay: ${final_amount}")

#this is a bit simpler than i realized but i need more practice