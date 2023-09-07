# Demonstration of a count-controlled while-loop
i = 2	
while i <= 40:
    print(i)			
    i = i + 2

# Demonstration of a sentinel-controlled while-loop
sum = 0
num = int(input("Enter number: "))
while num > 0:
    sum += num
    num = int(input("Enter number: "))
print ("Total:", sum)
