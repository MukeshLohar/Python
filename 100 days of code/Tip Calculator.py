#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the Tip calculater :)")
amount = int(input("What was your bill aomunt ?:"))
tip_percentage = float(input("what percentage for Tip :"))
people = int(input("how many ppl tip should be divide :"))

Bill_amount= (amount /people) * (1 +tip_percentage/100)
print(f"Bill amount for eeach person is {round(Bill_amount,2):.2f}")