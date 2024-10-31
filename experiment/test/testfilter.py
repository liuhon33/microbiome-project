# This is a sample from the definition

"""Filter a table based on a function or iterable.

Parameters
----------
ids_to_keep : iterable, or function(values, id, metadata) -> bool
    If a function, it will be called with the values of the
    sample/observation, its id (a string) and the dictionary
    of metadata of each sample/observation, and must return a
    boolean. If it's an iterable, it must be a list of ids to
    keep.
axis : {'sample', 'observation'}, optional
    It controls whether to filter samples or observations and
    defaults to "sample".
invert : bool, optional
    Defaults to ``False``. If set to ``True``, discard samples or
    observations where `ids_to_keep` returns True
inplace : bool, optional
    Defaults to ``True``. Whether to return a new table or modify
    itself.

Returns
-------
biom.Table
    Returns itself if `inplace`, else returns a new filtered table.

Raises
------
UnknownAxisError
    If provided an unrecognized axis.

Examples
--------
>>> import numpy as np
>>> from biom.table import Table

Create a 2x3 BIOM table, with observation metadata and sample
metadata:

>>> data = np.asarray([[0, 0, 1], [1, 3, 42]])
>>> table = Table(data, ['O1', 'O2'], ['S1', 'S2', 'S3'],
...               [{'full_genome_available': True},
...                {'full_genome_available': False}],
...               [{'sample_type': 'a'}, {'sample_type': 'a'},
...                {'sample_type': 'b'}])

Define a function to keep only samples with sample_type == 'a'. This
will drop sample S3, which has sample_type 'b':

>>> filter_fn = lambda val, id_, md: md['sample_type'] == 'a'

Get a filtered version of the table, leaving the original table
untouched:

>>> new_table = table.filter(filter_fn, inplace=False)
>>> print(table.ids())
['S1' 'S2' 'S3']
>>> print(new_table.ids())
['S1' 'S2']

Using the same filtering function, discard all samples with sample_type
'a'. This will keep only sample S3, which has sample_type 'b':

>>> new_table = table.filter(filter_fn, inplace=False, invert=True)
>>> print(table.ids())
['S1' 'S2' 'S3']
>>> print(new_table.ids())
['S3']

Filter the table in-place using the same function (drop all samples
where sample_type is not 'a'):

>>> table.filter(filter_fn)
2 x 2 <class 'biom.table.Table'> with 2 nonzero entries (50% dense)
>>> print(table.ids())
['S1' 'S2']

Filter out all observations in the table that do not have
full_genome_available == True. This will filter out observation O2:

>>> filter_fn = lambda val, id_, md: md['full_genome_available']
>>> table.filter(filter_fn, axis='observation')
1 x 2 <class 'biom.table.Table'> with 0 nonzero entries (0% dense)
>>> print(table.ids(axis='observation'))
"""