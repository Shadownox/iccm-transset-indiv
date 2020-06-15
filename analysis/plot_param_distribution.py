import pandas as pd
import numpy as np
import ccobra
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# read the param configuration file
params_df = pd.read_csv("parameterization/param_configs.csv", sep=";")

# Map for the NVC aversion values
nvc_aversion_values = {
    0 : "None",
    0.5 : "Low",
    1: "High"
}

# Storage for NVC aversion
nvc_aversion_dict = {
    "None" : 0,
    "Low" : 0,
    "High" : 0
}

# Storage for anchor
anchor_dict = {
    "First" : 0,
    "Most recent" : 0
}

# Storage for the particularity rule
particularity_dict = {
    "True" : 0,
    "False" : 0
}

# Storage for the negativity rule
negativity_dict = {
    "True" : 0,
    "False" : 0
}

# Iterate over the param configs
for _, row in params_df.iterrows():
    # re-instantiate configurations
    params = eval(row["params"])
    
    # iterate over each single param config
    for param_config in params:
        # Count parameter assignments in the storage dictionaries
        nvc_aversion_dict[nvc_aversion_values[param_config[0]]] += 1 / len(params)
        anchor_dict[param_config[1].replace("first", "First")
            .replace("most-recent", "Most recent")] += 1 / len(params)
        particularity_dict[str(param_config[2])] += 1 / len(params)
        negativity_dict[str(param_config[3])] += 1 / len(params)

# Plot the parameter distributions
f = plt.figure(figsize=(7, 3))

sns.set(palette="colorblind")
sns.set_style("whitegrid", {'axes.grid' : True})

top1 = plt.subplot2grid((1,4), (0,0), colspan=1)
top2 = plt.subplot2grid((1,4), (0,1), colspan=1)
bot1 = plt.subplot2grid((1,4), (0,2), colspan=1)
bot2 = plt.subplot2grid((1,4), (0,3), colspan=1)

top1.bar(*zip(*nvc_aversion_dict.items()), color="C0")
top1.set_ylabel("Participants")
top1.set_xlabel("$p_{aversion}$")
top1.set(ylim=(0,90))

top2.bar(*zip(*anchor_dict.items()), color="C1")
top2.set_ylabel("")
top2.set_yticklabels([])
top2.set_xlabel("$p_{anchor}$")
top2.set(ylim=(0,90))

bot1.bar(*zip(*particularity_dict.items()), color="C2")
bot1.set_xlabel("$p_{part}$")
bot1.set_yticklabels([])
bot1.set(ylim=(0,90))

bot2.bar(*zip(*negativity_dict.items()), color="C3")
bot2.set_xlabel("$p_{neg}$")
bot2.set_ylabel("")
bot2.set_yticklabels([])
bot2.set(ylim=(0,90))

plt.tight_layout()
plt.savefig('coverage_params.pdf')
plt.show()
