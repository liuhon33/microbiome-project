import numpy as np
from biom.table import Table
dt_rich = Table(np.array([[5, 6, 7],
                          [8, 9, 10],
                          [11, 12, 13]]),
                ['1', '2', '3'],
                ['a', 'b', 'c'],
                [{'taxonomy': ['k__a', 'p__b']},
                {'taxonomy': ['k__a', 'p__c']},
                {'taxonomy': ['k__a', 'p__c']}],
                [{'barcode': 'aatt'},
                {'barcode': 'ttgg'},
                {'barcode': 'aatt'}])
bin_f = lambda id_, x: x['taxonomy'][0]
obs_phy = dt_rich.collapse(bin_f,
                           norm=False,
                           min_group_size=1,
                           axis='observation').sort(axis='observation')