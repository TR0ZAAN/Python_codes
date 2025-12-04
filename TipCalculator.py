print("Welcome to the tip calculator")
bill= float(input("What is your bill?"))
tip= float(input("What is the percentage tip you want to add? 10 12 15 20"))
bill_includes_tip = bill + (bill * (1+tip))
print("Total amount including bill" + str(bill_includes_tip))
people=int(input("How many members are there to split the bill"))
bill_per_person = bill_includes_tip / people

print("Total amount including bill per person" + str(bill_per_person))