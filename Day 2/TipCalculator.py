print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15"))
number_of_people = int(input("How many people to split the bill?"))

tip_percentage = tip/ 100
tip_amount = bill*tip_percentage
total_bill = bill+tip_amount
bill = total_bill/number_of_people
bill = round(bill, 2)

print(f"Each person should pay:  ${bill}")
