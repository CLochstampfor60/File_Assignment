#question_2.py
# Question (2) (Total: 100 points)  
# Write a program to read in a file containing numbers. Each line is composed of only one single number.
# You should create an output file containing the square of each number from the first file.
# Ex.: 
# input File:
# 1
# 5
# 2
# 4

# Output File:
# 1
# 25
# 4
# 16

input_number_file = "inputFile2.txt"
output_number_file = "outputFile2.txt"

try:
    with open(input_number_file, 'r') as infile, open(output_number_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            squared = number ** 2
            outfile.write(str(squared) + '\n')
    print(f"Successfully processed '{input_number_file}' and created '{output_number_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_number_file} was not found.")