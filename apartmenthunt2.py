# This program determines an apartment renter's qualifications

# Input
income   = float(input("Monthly income: "))
jobYears = int(input("Years on job: "))
creditScore = int(input("Years credit score: "))

# Determine qualifications for rental.  Write appropriate feedback.
if (income > 5000 and jobYears > 2) or (creditScore > 700 and jobYears > 1):
    print("Congratulations, rental application accepted")
else:
    print("Sorry, application rejected")
