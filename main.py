#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


#My code
# print("Welcome to the tip calculator!\n")
# total_bill = float(input("What was the total bill? $"))
# tip = int(input("How much % tip would you like to give? "))
# people = int(input("How many people to split the bill? "))
# percent_tip = tip / 100 + 1
# final = round(total_bill * percent_tip / people, 2)
# print(f"Each person should pay: ${final}")

#Answer Key
# print("Welcome to the tip calculator!\n")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")

#Final Form
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $"))
tip = int(input("How much % tip would you like to give? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
formated_final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${formated_final_amount}")