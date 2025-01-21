import pandas as pd

# Read the CSV file
input_file = "test.csv"  # Replace with your file name
output_file = "output.csv"  # Replace with your desired output file name

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Drop the first column
df = df.iloc[:, 1:]

# Save the updated DataFrame back to a CSV file
df.to_csv(output_file, index=False)

print(f"Saved the updated CSV file as {output_file}")
