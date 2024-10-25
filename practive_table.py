import numpy as np
from biom.table import Table
data = np.arange(40).reshape(10, 4)
sample_ids = ['S%d' % i for i in range(4)]
observ_ids = ['O%d' % i for i in range(10)]
sample_metadata = [{'environment': 'A'}, {'environment': 'B'},
                   {'environment': 'A'}, {'environment': 'B'}]
observ_metadata = [{'taxonomy': ['Bacteria', 'Firmicutes']},
                   {'taxonomy': ['Bacteria', 'Firmicutes']},
                   {'taxonomy': ['Bacteria', 'Proteobacteria']},
                   {'taxonomy': ['Bacteria', 'Proteobacteria']},
                   {'taxonomy': ['Bacteria', 'Proteobacteria']},
                   {'taxonomy': ['Bacteria', 'Bacteroidetes']},
                   {'taxonomy': ['Bacteria', 'Bacteroidetes']},
                   {'taxonomy': ['Bacteria', 'Firmicutes']},
                   {'taxonomy': ['Bacteria', 'Firmicutes']},
                   {'taxonomy': ['Bacteria', 'Firmicutes']}]
table = Table(data, observ_ids, sample_ids, observ_metadata,
              sample_metadata, table_id='Example Table')
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
filter_f = lambda values, id_, md: md['environment'] == 'A'
env_a = normed.filter(filter_f, axis='sample', inplace=False)


# practice
# filter the "normed" table based on the bacteria type
filter_g = lambda values, id_, md: md['taxonomy'] == ['Bacteria', 'Proteobacteria']
pro_bac = normed.filter(filter_g, axis='observation', inplace=False)

# test_filter # what does this filter do?
filter_h = lambda values, id_, md: md['taxonomy']
abc = table.filter(filter_h, axis='observation', inplace=False)

dict(abc.metadata('O1', 'observation'))
dict(table.metadata('O1', 'observation'))
dict(abc.metadata('S1', 'sample'))
dict(table.metadata('S1', 'sample'))

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