import json
from biom import load_table
from biom import Table

def print_sample_abundance(table, sample_id, threshold = 0.001, truncate_length = 5):
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
    
    # Retrieve observation metadata as a DataFrame
    observation_metadata = table.metadata_to_dataframe('observation')
    
    # Prepare data for output
    abundance_data = []
    for otu_id in otu_ids:
        abundance = table.get_value_by_ids(otu_id, sample_id)
        if abundance >= threshold:
            # Retrieve taxonomy for the OTU
            taxonomy = observation_metadata.loc[otu_id].tolist()
            # Truncate OTU ID
            truncated_otu_id = otu_id[:truncate_length]
            abundance_data.append((truncated_otu_id, *taxonomy, abundance))
    
    # Define header
    header = ['OTU ID', 'taxonomy_0', 'taxonomy_1', 'taxonomy_2', 
              'taxonomy_3', 'taxonomy_4', 'taxonomy_5', 'taxonomy_6', 'Relative Abundance']
    
    # Print the table
    print(f"\nAbundance Table for Sample: {sample_id}")
    print('\t'.join(header))
    for row in abundance_data:
        row_str = '\t'.join([str(item) for item in row])
        print(row_str)