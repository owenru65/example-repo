#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line

print("Welcome to the tip calculator")
tot_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12 or 15:  "))
ppl=int(input("How many people to split the bill? "))

individual_bill=round(((tot_bill*(1+tip/100))/ppl),2)

individual_amt="{:.2f}".format(individual_bill)

print(f"\nEach person should pay : ${individual_amt}\n")
