import numpy as np
from biom import Table
import pandas as pd

# Step 1: Define Data Matrix
# 15 observations (OTUs) x 6 samples
np.random.seed(42)  # For reproducibility
data = np.random.randint(50, 500, size=(15, 6))

# Step 2: Define IDs
sample_ids = [f'Sample{i}' for i in range(1, 7)]
observ_ids = [f'OTU{i}' for i in range(1, 16)]

# Step 3: Define Metadata

# Sample Metadata with multiple fields
sample_metadata = [
    {'environment': 'Forest', 'location': 'North', 'collection_date': '2023-07-01'},
    {'environment': 'Lake', 'location': 'South', 'collection_date': '2023-07-02'},
    {'environment': 'Desert', 'location': 'East', 'collection_date': '2023-07-03'},
    {'environment': 'Forest', 'location': 'West', 'collection_date': '2023-07-04'},
    {'environment': 'Lake', 'location': 'North', 'collection_date': '2023-07-05'},
    {'environment': 'Desert', 'location': 'South', 'collection_date': '2023-07-06'}
]

# Observation Metadata with multiple fields
observ_metadata = [
    {'taxonomy': ['Bacteria', 'Firmicutes', 'Bacilli'], 'functional_group': 'Fermenter', 'growth_rate': 'Fast'},
    {'taxonomy': ['Bacteria', 'Proteobacteria', 'Alpha'], 'functional_group': 'Degrader', 'growth_rate': 'Medium'},
    {'taxonomy': ['Bacteria', 'Actinobacteria', 'Actinomyces'], 'functional_group': 'Producer', 'growth_rate': 'Slow'},
    {'taxonomy': ['Bacteria', 'Bacteroidetes', 'Bacteroides'], 'functional_group': 'Detritivore', 'growth_rate': 'Fast'},
    {'taxonomy': ['Bacteria', 'Firmicutes', 'Clostridia'], 'functional_group': 'Fermenter', 'growth_rate': 'Medium'},
    {'taxonomy': ['Bacteria', 'Proteobacteria', 'Beta'], 'functional_group': 'Degrader', 'growth_rate': 'Slow'},
    {'taxonomy': ['Bacteria', 'Actinobacteria', 'Streptomyces'], 'functional_group': 'Producer', 'growth_rate': 'Fast'},
    {'taxonomy': ['Bacteria', 'Bacteroidetes', 'Prevotella'], 'functional_group': 'Detritivore', 'growth_rate': 'Medium'},
    {'taxonomy': ['Bacteria', 'Firmicutes', 'Lactobacilli'], 'functional_group': 'Fermenter', 'growth_rate': 'Slow'},
    {'taxonomy': ['Bacteria', 'Proteobacteria', 'Gamma'], 'functional_group': 'Degrader', 'growth_rate': 'Fast'},
    {'taxonomy': ['Bacteria', 'Actinobacteria', 'Mycobacterium'], 'functional_group': 'Producer', 'growth_rate': 'Medium'},
    {'taxonomy': ['Bacteria', 'Bacteroidetes', 'Bacteroides'], 'functional_group': 'Detritivore', 'growth_rate': 'Slow'},
    {'taxonomy': ['Bacteria', 'Firmicutes', 'Bacilli'], 'functional_group': 'Fermenter', 'growth_rate': 'Fast'},
    {'taxonomy': ['Bacteria', 'Proteobacteria', 'Delta'], 'functional_group': 'Degrader', 'growth_rate': 'Medium'},
    {'taxonomy': ['Bacteria', 'Actinobacteria', 'Corynebacterium'], 'functional_group': 'Producer', 'growth_rate': 'Slow'}
]
table = Table(
    data,
    observ_ids,
    sample_ids,
    observ_metadata,
    sample_metadata,
    table_id='Advanced Example Table'
)
"""
Table is a class created in the file biom.table.
now we created an instance table using the class Table
normed = table.norm(axis='sample', inplace=False)
result of this after we created env_a is
>>> print(env_a)
    # Constructed from biom file
#OTU ID S0      S2
O0      0.0     0.01
O1      0.022222222222222223    0.03
O2      0.044444444444444446    0.05
O3      0.06666666666666667     0.07
O4      0.08888888888888889     0.09
O5      0.1111111111111111      0.11
O6      0.13333333333333333     0.13
O7      0.15555555555555556     0.15
O8      0.17777777777777778     0.17
O9      0.2     0.19
""

however, if we change the axis as "observation"
>>> print(env_a)
Constructed from biom file here is the output
#OTU ID S0      S2
O0      0.0     0.3333333333333333
O1      0.18181818181818182     0.2727272727272727
O2      0.21052631578947367     0.2631578947368421
O3      0.2222222222222222      0.25925925925925924
O4      0.22857142857142856     0.2571428571428571
O5      0.23255813953488372     0.2558139534883721
O6      0.23529411764705882     0.2549019607843137
O7      0.23728813559322035     0.2542372881355932
O8      0.23880597014925373     0.2537313432835821
O9      0.24    0.25333333333333335
"""
normed = table.norm(axis='sample', inplace=False)

# filter the "normed" table based on the environment
filter_f = lambda values, id_, md: md['environment'] == 'Lake'
env_a = normed.filter(filter_f, axis='sample', inplace=False)


# practice
# filter the "normed" table based on the bacteria type
filter_g = lambda values, id_, md: md['taxonomy'] == ['Bacteria', 'Actinobacteria', 'Corynebacterium']
pro_bac = normed.filter(filter_g, axis='observation', inplace=False)

# test_filter # what does this filter do?
# filter_h does not do anything
filter_h = lambda a, b, c: c['taxonomy']
abc = table.filter(filter_h, axis='observation', inplace=False)

# another filter
filter_i = lambda values, id_, md: md['taxonomy'][1] == 'Firmicutes'
firm_bac = abc = table.filter(filter_i, axis='observation', inplace=False)
firm_bac


dict(abc.metadata('Sample1', 'observation'))
dict(table.metadata('OTU1', 'observation'))
dict(abc.metadata('Sample1', 'sample'))
dict(table.metadata('OTU', 'sample'))

"""
>>> abc == table
True
"""

# find the metadata for a specific row(observation) or colomn(sample)
table.metadata('S1', 'sample')
dict(table.metadata('S1', 'sample'))
dict(table.metadata('O1', 'observation'))
table.matrix_data

# export the metadata to a dataframe
table.metadata_to_dataframe('observation')
table.metadata_to_dataframe('sample')

"""

method partition, like filter, accepts a function.
However, unlike the filter, partition function
only passes the corresponding ID and metadata to
the function

"""
part_f = lambda id_, md: md['environment']
env_tables = table.partition(part_f, axis='sample')
for partition, env_table in env_tables:
    print(partition, env_table.sum('sample'))

# set up the transform
transform_f = lambda v, i, m: np.where(v % 3 == 0, v, 0)
mult_of_three = tform = table.transform(transform_f, inplace = False)
print(mult_of_three)

"""
The collapse method allows to aggregate observations or samples
based on a specific criterion.

example: collapse observatoins(OTU) based on their
phylum-level taxonomy
"""
# Define the index for the phylum level in taxonomy
phylum_idx = 1
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
collapsed = mult_of_three.collapse(collapse_f, axis='observation')
print(collapsed)

