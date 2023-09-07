# This program performs a simple division.  It first
# validates the divisor.

# Input division operands
dividend = float(input("Enter dividend: "))
divisor  = float(input("Enter divisor: "))

# Validate to insure non-zero divisor
while divisor == 0:
    print ("Invalid operation - Divisor cannot be zero.")
    divisor  = float(input("Re-enter divisor: "))

# After input validated, perform division and display quotient
quotient = dividend / divisor
print("Quotient: ", quotient)
