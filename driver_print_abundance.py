import json
from biom import load_table
from biom import Table
from print_sample_abundance import print_sample_abundance

table = load_table('dataset/test_export.json')

### PLAYING WITH THE TABLE
# Get table shape
num_observations, num_samples = table.shape
print(f"Number of Observations (OTUs): {num_observations}")
print(f"Number of Samples: {num_samples}")

# Access sample IDs
sample_ids = table.ids(axis='sample')
print(f"Sample IDs: {sample_ids[:5]} ...")  # Display first 5 sample IDs

# Access metadata
# sample_metadata = table.metadata_to_dataframe('sample')
observation_metadata = table.metadata_to_dataframe('observation')
print(observation_metadata)

# Get the metadata associated with a specific OTU
dict(table.metadata('TACGGAAGGTCCGGGCGTTATCCGGATTTATTGGGTTTAAAGGGAGCGCAGGCCGTCCTTTAAGCGTGCTGTGAAATGCCGCGGCTCAACCGTGGCACTGCAGCGCGAACTGGGGGACTTGAGTA', 'observation'))

# Example usage
sample_id = '10317.000002606'
print_sample_abundance(table, sample_id)



