#question_1.py
# Define the names of the input and output files
input_filename = 'inputFile.txt'
output_filename = 'outputFile.txt'

try:
    # Open the input file for reading and the output file for writing
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        # Loop through each line in the input file
        for line in infile:
          # Write the line to the output file twice
            clean_line = line.strip()
            outfile.write(clean_line + '\n')
            outfile.write(clean_line + '\n')
    print(f"Successfully processed '{input_filename}' and created '{output_filename}'.")

except FileNotFoundError:  
    print(f"Error: The file '{input_filename}' was not found.")