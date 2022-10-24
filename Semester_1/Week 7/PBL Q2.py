"""
Milan, Nikola & Tosin 07/11/2019
PBL Q2: Grades
"""
# Range 0 to 100, sentinel value is -1

# Other
number_of_grades = 0
grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_e = 0
grade_f = 0

# Inputs
grade = int(input("Please enter your grade: "))

# Processes
if 100 >= grade >= 0:
    if grade != -1:
        while grade != -1:
            number_of_grades += 1
            if grade >= 90:
                grade_a += 1
            elif grade_b >= 80:
                grade_b += 1
            elif grade >= 70:
                grade_c += 1
            elif grade >= 60:
                grade_d += 1
            else:
                grade_f += 1
        print("Total number of grades: ", number_of_grades)
        print("\n")
        print("Grade A's:", grade_a)
        print("Grade B's:", grade_b)
        print("Grade C's:", grade_c)
        print("Grade D's:", grade_d)
        print("Grade E's", grade_e)
        print("Grade F's", grade_f)
else:
    print("No data entered")
