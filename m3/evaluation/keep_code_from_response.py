import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract codes from response file.')
parser.add_argument('file', type=str, help='The file containing the response data.')

# Parse arguments
args = parser.parse_args()

# Read the input file and extract codes
with open(args.file, 'r') as file:
    lines = file.readlines()

# Open the same file in write mode to overwrite it
with open(args.file, 'w') as file:
    for line in lines:
        # Split the line into parts and get the code (third part)
        parts = line.split()
        if len(parts) > 2:
            code = parts[2]
            # Write the code to the file
            file.write(code + '\n')

print(f"Filtered codes have been saved to {args.file}.")