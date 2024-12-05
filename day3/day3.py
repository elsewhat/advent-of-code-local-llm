import re

# Read the input data from file
with open('input.txt', 'r') as f:
    data = f.read()

# Define the pattern for matching "mul(X,Y)"
pattern = r'mul\(\d{1,3},\d{1,3}\)'

# Find all matches in the data
matches = re.findall(pattern, data)

# Initialize total sum
total = 0

# Process each match to extract X and Y, convert to integers, multiply, and add to total
for match in matches:
    # Extract X and Y from the match using another regular search
    x_str, y_str = re.search(r'mul\((\d{1,3}),(\d{1,3})\)', match).groups()
    x = int(x_str)
    y = int(y_str)
    product = x * y
    total += product

# Output the total sum
print(total)