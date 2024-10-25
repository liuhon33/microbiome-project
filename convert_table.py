import json
from biom import load_table
from biom import Table

"""
# Load the JSON file DO I REALLY NEED THIS???
with open('dataset/test_export.json', 'r') as f:
    biom_json = json.load(f)
"""


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

def print_sample_abundance(table, sample_id, threshold = 0.001):
    """
    Prints the abundance table for a specified sample.
    
    Parameters:
    - table (biom.Table): The BIOM Table instance.
    - sample_id (str): The ID of the sample to retrieve abundances for.
    
    Outputs:
    - Prints the OTU ID and its relative abundance in the specified sample.
    """
    # Check if the sample ID exists in the table
    if sample_id not in table.ids(axis='sample'):
        raise ValueError(f"Sample ID '{sample_id}' not found in the table.")
    
    
    # Get all OTU IDs
    otu_ids = table.ids(axis='observation')
    
    # Print header
    print(f"\nAbundance Table for Sample: {sample_id}")
    print("OTU ID\tRelative Abundance")
    
    # Iterate over all OTUs and print their abundance in the specified sample
    for otu_id in otu_ids:
        abundance = table.get_value_by_ids(otu_id, sample_id)
        if abundance >= threshold:
            print(f"{otu_id}\t{abundance}")

# Example usage
sample_id = '10317.000002606'
print_sample_abundance(table, sample_id)




"""


print("\nObservation Metadata:")
print(observation_metadata.head(6))
"""




