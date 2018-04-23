# CTI-110
# P5HW1: Test Average and Grades
# Lorenzo Warren
# April 22, 2018


# Program using ten point grading scale
A = 90-100 
B = 80-89 
C = 70-79
D = 60-69

def main():

# The Grades 
    for grade in range (1, 5):

    # The average grade for five test scores.
        grade = float(input('Enter test grade:'))
    if grade == 90-100:
        print('The grade is an A')
    if grade == 80-89:
        print('The grade is a B')
    if grade == 70-79:
        print('the grade is a C')
    if grade == 60-69:
        print('The grade is a D')

    sum = sum / grade

# Display the average grades.
print('The average is:',  sum / grade)

# call the main function.
main()
