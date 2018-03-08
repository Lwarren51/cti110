# CTI-110
# P3T1 - Area of Rectangles
# Lorenzo Warren
# March 11, 2018

# Get the dimensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determie which has the greater area.
if area1 > area2:
    print ('Rectangle 1 has the greater area.')
else:
    if area2 > area1:
        print ('Rectangle 2 has the greater area.')
    else:
        print ('Both have the same area.')
