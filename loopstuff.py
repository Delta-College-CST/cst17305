#####################################################

# This program sums a sequence 1..n where n is
# defined by the user

endValue = int(input("Enter end value: "))

sum = 0

# Accumuldate series of numbers from 1..endValue
for num in range (1,endValue+1):
    sum = sum + num

print("Sum from: 1 to",endValue,"=",sum)

#####################################################
print("\n\n")   # Print blank separatory lines
#####################################################

# This program generates the first 20 perfect squares
# and perfect cubes 

print(" Number Square   Cube")
for n in range (1,21):
    print(" %4d   %4d    %4d" % (n, n*n, n**3) )

#####################################################
print("\n\n")   # Print blank separatory lines
#####################################################

# This program finds the largest perfect square under 1 million

number = 1   # Initialize to first perfect square

# Loop continues while latest perfect square remains under
# 1 million.  Most recent perfect square retained when
# 1 million exceeded.
while (number**2 < 1000000):
    lastSquare = number**2
    number = number + 1

print("Largest perfect square under 1 million",lastSquare)

#####################################################

