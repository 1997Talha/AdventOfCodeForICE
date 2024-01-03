import sys

def process_line(line):
    # Define the digits and a dictionary mapping words to their digit equivalents
    digits = [str(d) for d in range(10)]
    word_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    p1_digits, p2_digits = [], []

    # Check each character in the line and add to p1_digits and p2_digits if it's a digit
    for c in line:
        if c in digits:
            p1_digits.append(c)
            p2_digits.append(c)

    # Check for each word in the line and add its corresponding digit to p2_digits
    for word, digit in word_to_digit.items():
        if word in line:
            p2_digits.append(digit)

    return p1_digits, p2_digits

def main(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        data = file.read().strip()

    p1, p2 = 0, 0
    # Process each line of the file
    for line in data.split('\n'):
        p1_line_digits, p2_line_digits = process_line(line)
        # Add the first and last digit (if present) to p1 and p2 totals
        if p1_line_digits:
            p1 += int(p1_line_digits[0] + p1_line_digits[-1])
        if p2_line_digits:
            p2 += int(p2_line_digits[0] + p2_line_digits[-1])

    print(f"p1: {p1}, p2: {p2}")

if __name__ == "__main__":
    # Execute the main function with the file path provided as an argument
    main(sys.argv[1])
