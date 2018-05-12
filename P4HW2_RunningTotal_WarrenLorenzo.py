# CTI-110
# P4HW2 - Running Total
# Lorenzo Warren
# March 25, 2018


# Initialize the accumulator.
total = 0

# Get the series of numbers.
for numbers in range (1, 6):

    # Prompt the user.
    print ('Enter a numbers ? ')

    # Input the series of numbers.
    numbers = int(input () )

    # Add to total.
    total = total + numbers

# Display the total numbers.
print ('Total of', total, 'numbers.')


