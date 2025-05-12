print("Hey What's this is for tips ")
bill = float(input("What was the total bill? "))
tip = float(input("what percentage would you like to give? "))
people = int(input("How many people are splitting "))

# The first part is just the set up of the variables 
#this second part is the reason for the code working

tip_as_per = tip / 100
totaltip = bill * tip_as_per
total_bill = bill + totaltip
billper = total_bill / people
finalamount = round(billper,2)
print(f"Each person will pay {finalamount}")

#do about three more and go back in the thing and check