print("///////////////////////////////WEEKS LEFT IN YOUR LIFE///////////////////////////////")

#User input
userAge = int(input("How old are you\n"))
userHealthStatus = int(input("How healthy are you on a scale of 1 to 5: \n"))

if (userHealthStatus == 5):
    userLifeSpan = 90
elif (userHealthStatus == 4):
    userLifeSpan = 80
elif (userHealthStatus == 3):
    userLifeSpan = 70
elif (userHealthStatus <= 2):
    userLifeSpan = 65
else:
    print("You can't give a rating beyond the scope of the scale!")

#Calculating an approximate count of weeks left in user's life
totalWeeksInUserLife = userLifeSpan * 52
weeksExhaustedByTheUser = userAge * 52
weeksLeftForTheUser = totalWeeksInUserLife - weeksExhaustedByTheUser

if (userLifeSpan < 75):
    print(f"You approximately have {weeksLeftForTheUser} weeks left. A healthier lifestyle could increase the number of weeks :)")
else:
    print(f"You approximately have {weeksLeftForTheUser} weeks left.")