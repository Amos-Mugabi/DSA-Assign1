# No. 3

bill = float(input("Enter the bill amount: "))
tip = float(input("Enter the tip amount: "))
num_people = int(input("Enter the number of people: "))

total = bill + tip
amount_per_person = total / num_people

print("Amount paid per person: %.2f" % amount_per_person)

print("Total amount paid: %.2f" % total)
