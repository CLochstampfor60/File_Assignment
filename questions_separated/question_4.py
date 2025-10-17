#question_4.py
# Write a program to read in the grades of three Cybersecurity courses (CYSE 250 CYSE 270 CYSE 200T)
# of a set of students. Grades are separated by a space. Each line represents a student. Calculate the mean grade of every student and write it into an output file.
# Input File:
# 60 70 80
# 70 80 90
# 40 50 60

# Output File:
# 70
# 80
# 50

class_grades = 'class_grades.txt'
mean_grades = 'meanGrades.txt'

try:
    with open(class_grades, 'r') as infile, \
        open(mean_grades, 'w') as outfile:

        for line in infile:
            line = line.strip()

            if line:
                grades = list(map(int, line.split()))
                mean_grade = sum(grades) / len(grades)
                outfile.write(str(int(mean_grade)) + '\n')
    
    print(f"Successfully created '{mean_grades}', calculating each students' total .")

except FileNotFoundError:
    print(f"Error: The file '{class_grades}' was not found.")
except ValueError:
        print(f"Error: Ensure all data in '{class_grades}' are numbers.")
