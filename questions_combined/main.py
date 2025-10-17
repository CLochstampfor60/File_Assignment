# CYSE 250 Files Assignment - Complete Solutions
# This script creates all input files and runs all questions

# ===== CREATE INPUT FILES =====

def create_input_files():
    """Create all necessary input files for the assignment"""
    
    # Question 1: Input file with text lines
    with open('inputFile_q1.txt', 'w') as f:
        f.write("Python is fun.\n")
        f.write("I like programming.\n")
    
    # Question 2: Input file with numbers
    with open('inputFile_q2.txt', 'w') as f:
        f.write("1\n")
        f.write("5\n")
        f.write("2\n")
        f.write("4\n")
    
    # Question 3: First names file
    with open('firstNames.txt', 'w') as f:
        f.write("Jade\n")
        f.write("Chandler\n")
        f.write("Andy\n")
        f.write("Maggie\n")
    
    # Question 3: Last names file
    with open('lastNames.txt', 'w') as f:
        f.write("Moore\n")
        f.write("Anderson\n")
        f.write("Boateng\n")
        f.write("Bowles\n")
    
    # Question 4: Grades file
    with open('class_grades.txt', 'w') as f:
        f.write("60 70 80\n")
        f.write("70 80 90\n")
        f.write("40 50 60\n")
    
    print("All input files created successfully!\n")


# ===== QUESTION 1 =====

def question_1():
    """Duplicate each line in a file"""
    input_filename = 'inputFile_q1.txt'
    output_filename = 'outputFile_q1.txt'
    
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                clean_line = line.strip()
                outfile.write(clean_line + '\n')
                outfile.write(clean_line + '\n')
        
        print(f"Question 1: Successfully created '{output_filename}'")
        
        # Display output
        with open(output_filename, 'r') as f:
            print("Output:")
            print(f.read())
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")


# ===== QUESTION 2 =====

def question_2():
    """Square each number in a file"""
    input_filename = 'inputFile_q2.txt'
    output_filename = 'outputFile_q2.txt'
    
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                number = int(line.strip())
                squared = number ** 2
                outfile.write(str(squared) + '\n')
        
        print(f"Question 2: Successfully created '{output_filename}'")
        
        # Display output
        with open(output_filename, 'r') as f:
            print("Output:")
            print(f.read())
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except ValueError:
        print("Error: File contains non-numeric values.")


# ===== QUESTION 3 =====

def question_3():
    """Combine first and last names from two files"""
    first_names_file = 'firstNames.txt'
    last_names_file = 'lastNames.txt'
    output_filename = 'fullNames.txt'
    
    try:
        with open(first_names_file, 'r') as first_file, \
             open(last_names_file, 'r') as last_file, \
             open(output_filename, 'w') as outfile:
            
            for first_name, last_name in zip(first_file, last_file):
                first_name = first_name.strip()
                last_name = last_name.strip()
                
                if first_name and last_name:
                    full_name = first_name + ' ' + last_name
                    outfile.write(full_name + '\n')
        
        print(f"Question 3: Successfully created '{output_filename}'")
        
        # Display output
        with open(output_filename, 'r') as f:
            print("Output:")
            print(f.read())
    
    except FileNotFoundError:
        print(f"Error: One or both input files were not found.")
    except Exception as e:
        print(f"Error: {e}")


# ===== QUESTION 4 =====

def question_4():
    """Calculate mean grade for each student"""
    input_filename = 'class_grades.txt'
    output_filename = 'meanGrades.txt'
    
    try:
        with open(input_filename, 'r') as infile, \
             open(output_filename, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if line:  # Skip empty lines
                    grades = list(map(int, line.split()))
                    mean_grade = sum(grades) / len(grades)
                    outfile.write(str(int(mean_grade)) + '\n')
        
        print(f"Question 4: Successfully created '{output_filename}'")
        
        # Display output
        with open(output_filename, 'r') as f:
            print("Output:")
            print(f.read())
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except ValueError:
        print("Error: File contains non-numeric values.")
    except Exception as e:
        print(f"Error: {e}")


# ===== MAIN EXECUTION =====

if __name__ == "__main__":
    print("=" * 50)
    print("CYSE 250 Files Assignment")
    print("=" * 50)
    print()
    
    # Create all input files first
    create_input_files()
    
    # Run all questions
    print("-" * 50)
    question_1()
    print("-" * 50)
    question_2()
    print("-" * 50)
    question_3()
    print("-" * 50)
    question_4()
    print("-" * 50)
    
    print("\nAll questions completed!")