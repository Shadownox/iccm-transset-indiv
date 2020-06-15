import pandas as pd
import numpy as np
import ccobra
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CCOBRA evaluation data
result_df = pd.read_csv("ccobra_coverage_results/transset_ragni2016.csv")

# Load the CogSci2020 individualization results (mReasoner & PHM)
result_alt_df = pd.read_csv('ccobra_coverage_results/mreasoner_phm_ragni2016_cogsci2020indiv.csv')
result_alt_df = result_alt_df.loc[result_alt_df['model'].isin(['mReasoner', 'PyPHM'])]
result_df = pd.concat([result_df, result_alt_df])

# Normalize model names
result_df['model'] = result_df['model'].replace({
    'PyPHM': 'PHM (fit)',
    'mReasoner': 'mReasoner (fit)',
    'MFAModel': 'MFA',
    'Uniform': 'Random'
})

# Mean the data
subj_df = result_df.groupby(
    ['model', 'id'], as_index=False)['hit'].agg('mean')

order_df = subj_df.groupby(['model'], as_index=False)['hit'].agg('mean')
order = order_df.sort_values('hit')['model']

# Prepare for plotting
sns.set(style="whitegrid", palette='colorblind')
plt.figure(figsize=(9, 4))

# Color definition
point = [0.3, 0.6, 0.8]
box = [0.3, 0.6, 0.8, 0.5]

# Plot the data
sns.swarmplot(x="model", y="hit", data=subj_df, order=order,
              dodge=True, linewidth=0.5, size=5, edgecolor=[0.3,0.3,0.3], color=point, zorder=1)

ax = sns.boxplot(x="model", y="hit", data=subj_df, order=order,
                 showcaps=False,boxprops={'facecolor': box, "zorder":10},
                 showfliers=False,whiskerprops={"zorder":10}, linewidth=1, color="black",
                 zorder=10)

plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.xlabel('')
ax.set_ylabel('Coverage', size=16)
ax.tick_params(labelsize=14)

plt.tight_layout()
plt.savefig('coverage_swarmplot.pdf')
plt.show()
