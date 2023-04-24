from datetime import datetime

now = datetime.now() # Get the current datetime object

# Format the datetime object as a string with a custom format
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted time:", formatted_time)


# Open the input file for reading and the output file for writing
with open('test.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # Remove existing whitespace from the end of the line
        line = line.rstrip()
        # Add new whitespace to the end of the line
        line += ' ' * 10 # Add 10 spaces to the end of the line
        # Write the modified line to the output file
        output_file.write(line + '\n')
