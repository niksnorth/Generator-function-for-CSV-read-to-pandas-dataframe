import pandas as pd
import numpy as np
import csv
from collections import defaultdict, OrderedDict, Counter

def get_data(csv_fname, chunk_size=1000000):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1MB."""
    with open(csv_fname, "r") as airport_records:
        for record in csv.reader(airport_records):
            yield record

filename = "airports2.csv"
iter_data = iter(get_data(filename, 1000000))

colks= next(iter_data)  # Skipping the column names
colk = list(colks)
print(colk)

df = pd.DataFrame()

for row in iter_data:
    df2 = pd.DataFrame(row, index=list(col))
    df2=df2.T
    df = df.append(df2)
	
index2=pd.Index(range(0, len(df['id'])))
df.set_index(index2, inplace=True)
print(df.head())

print(df.tail())
