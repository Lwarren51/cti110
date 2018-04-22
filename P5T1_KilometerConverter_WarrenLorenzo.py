# CTI-110
# P5T1 - Kilometer Converter
# Lorenzo Warren
# APril 22, 2018

# This program converts kilometers to miles. 
CONVERSION_FACTOR = 0.6214

# This main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function.
main()
    
