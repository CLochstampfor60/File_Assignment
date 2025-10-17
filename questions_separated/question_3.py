# Write a program to read in two files. The first file contains the first name of a set of students.  The second file contains the last name of a set of students. Create a third file containing the full names of the students.

# Input Files: First Names and Last Names
# First Names:
# Jade
# Chandler
# Andy
# Maggie

# Last Names:
# Moore
# Anderson
# Boateng
# Bowles

# Output File: Full Names
# Full Names:
# Jade Moore
# Chandler Anderson
# Andy Boateng
# Maggie Bowles

first_names = "first_names.txt"
last_names = "last_names.txt"
full_names = "full_names.txt"

try:
    with open(first_names, 'r') as firstFile, \
        open(last_names, 'r') as secondFile, \
        open(full_names, 'w') as outfile:

        for first_name, last_name in zip(firstFile, secondFile):
            first_name = first_name.strip()
            last_name = last_name.strip()

            if first_name and last_name:
                full_name = first_name + ' ' + last_name
                outfile.write(full_name + '\n')
    
    print(f"Successfully created '{full_names}' with the combined names.")


except FileNotFoundError:
    print(f"Error: Either '{first_names}' and/or '{last_names}' were not found.")