print("~~~~~~~~~~~~~~~~TIP CALCULATOR~~~~~~~~~~~~~~~~")

# Prompting the user to enter the total bill amount
bill = float(input("Enter the total bill: $"))

# Prompting the user to enter the tip percentage
userTipChoice = int(input("How much would you like to tip (in percent)? "))

# Prompting the user to enter the number of people to split the bill
totalNumberOfPeople = int(input("How many people to split the bill? "))

# Calculating the tip amount
tipAmount = (userTipChoice / 100) * bill

# Calculating the total bill including the tip
totalBill = bill + tipAmount

# Calculating the amount each person needs to pay
billOfEachPerson = round(totalBill / totalNumberOfPeople, 2)

# Displaying the amount each person needs to pay
print(f"Each person pays ${billOfEachPerson}")
