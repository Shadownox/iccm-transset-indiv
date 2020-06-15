import pandas as pd
import numpy as np
import scipy as sp
import scipy.stats as ss

# Load data
df = pd.read_csv('ccobra_coverage_results/transset_ragni2016.csv')

# Extract standard transset
ts_accs = df.loc[df['model'] == 'TransSet'].groupby('id', as_index=False)['hit'].agg('mean')['hit'].values
ts_fit_accs = df.loc[df['model'] == 'TransSet (fit)'].groupby('id', as_index=False)['hit'].agg('mean')['hit'].values

# Compute Mann-Whitney U test
print(ss.mannwhitneyu(ts_accs, ts_fit_accs))