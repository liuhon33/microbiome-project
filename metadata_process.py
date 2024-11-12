import pandas as pd
import os

# Path to your TSV file
file_path = './dataset/metadata.tsv'

# Read the TSV file into a pandas DataFrame
df = pd.read_csv(file_path, sep='\t')

# Total number of rows in the DataFrame
total_rows = len(df)

# Calculate the number of 'Not provided' entries per column
not_provided_counts = (df == 'Not provided').sum()

# Calculate the percentage of 'Not provided' entries per column
not_provided_percentages = (not_provided_counts / total_rows) * 100

# Create a DataFrame with the results
result_df = pd.DataFrame({
    'column_name': not_provided_percentages.index,
    'not_provided_percentage': not_provided_percentages.values
})

# Round the percentages to two decimal places
result_df['not_provided_percentage'] = result_df['not_provided_percentage'].round(2)

# Display the result
print(result_df)


# Define the output file path
output_file_path = './dataset/not_provided_summary.tsv'

try:
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # Save the DataFrame to a TSV file
    result_df.to_csv(output_file_path, sep='\t', index=False)
    print(f"\nResult successfully saved to {output_file_path}")
except Exception as e:
    print(f"Error: Could not save the file to {output_file_path}.")
    print(e)
