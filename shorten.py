# Read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Filter the lines by legnth
filtered_lines = [line for line in lines if len(line.strip()) <= 6]

# Write the filtered lines to a new file
with open('shortened.txt', 'w') as file:
    file.writelines(filtered_lines)
