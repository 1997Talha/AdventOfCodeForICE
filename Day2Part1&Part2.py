import sys
from collections import defaultdict

# Open and read the file specified in the command line argument
with open(sys.argv[1], 'r') as file:
    data = file.read().strip()

p1 = 0
p2 = 0
# Define the maximum allowed number of cubes for each color
max_cubes = {'red': 12, 'green': 13, 'blue': 14}

# Process each line of the file
for line in data.split('\n'):
    is_valid = True
    id_, events = line.split(':')
    max_count = defaultdict(int)

    # Process each event and update the max count for each color
    for event in events.split(';'):
        for ball_info in event.split(','):
            count, color = map(str.strip, ball_info.split())
            count = int(count)
            max_count[color] = max(max_count[color], count)
            # Check if count exceeds the limit for the color
            if count > max_cubes.get(color, 0):
                is_valid = False

    # Calculate the score for the line
    score = 1
    for count in max_count.values():
        score *= count
    p2 += score

    # Add to p1 if the line is valid
    if is_valid:
        p1 += int(id_.split()[-1])

print(f"p1: {p1}")
print(f"p2: {p2}")
