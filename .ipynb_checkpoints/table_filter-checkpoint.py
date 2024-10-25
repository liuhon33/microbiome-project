import numpy as np
from biom.table import Table
data = np.asarray([[0, 0, 1], [1, 3, 42]])
table = Table(data, ['O1', 'O2'], ['S1', 'S2', 'S3'],
            [{'full_genome_available': True},
                {'full_genome_available': False}],
            [{'sample_type': 'a'}, {'sample_type': 'a'},
               {'sample_type': 'b'}]
               )
"""
This is the original table, consisting of 2 observations, i.e. 2 rows,
consisting of 3 samples, i.e. 3 colomns
Think each row as one bacteria
Think each column as one sample
"""
filter_fn = lambda val, id_, md: md['sample_type'] == 'a'
new_table = table.filter(filter_fn, inplace=False)
print(table.ids())
print(new_table.ids())
table.filter(filter_fn)