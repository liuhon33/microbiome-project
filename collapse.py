import json
from biom import load_table
from biom import Table
from input_sample_output_table.print_sample_abundance import print_sample_abundance

table = load_table('dataset/test_export.json')

# Define the index for the phylum level in taxonomy
phylum_idx = 2
# Define the collapse function
# slice it upto phylum_indx + 1, but not including
collapse_f = lambda id_, md: '; '.join(md['taxonomy'][:phylum_idx + 1])
# Apply the collapse to the normalized table
"""
by comparing the output between mult_of_three
and collapsed
notice that 
for each sample
1. sort all the rows that are Bacteria; Firmicutes
2. add the number together
3. divided by the number of rows derived in 1
this number is the condensed number
"""
collapsed = table.collapse(collapse_f, axis='observation', norm=False)

# Retrieve all sample IDs from the collapsed table
all_sample_ids = collapsed.ids(axis='sample')

# Select the first five sample IDs
first5_sample_ids = all_sample_ids[:5]
print(f"\nSelected Sample IDs (First 5): {first5_sample_ids}")

# Define a filter function to keep only the first five sample IDs
def keep_first5(values, id_, md):
    return id_ in first5_sample_ids

# Apply the filter to create a subset table with only the first five samples
subset_table = collapsed.filter(keep_first5, axis='sample', inplace=False)
print(subset_table)

# Export the subset_table to a TSV file using direct_io
output_filename = 'subset_table_class.tsv'
with open(output_filename, 'w') as f:
    collapsed.to_tsv(direct_io=f)
print(f"\nSubset table successfully exported to '{output_filename}'.")

# TO DO: Write a for loop for exporting these data