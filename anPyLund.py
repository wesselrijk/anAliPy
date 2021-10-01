"""
Author: Wessel Rijk
This program produces a Lund plane from a .root file of a SoftDrop dataset.
"""

# list of imports
import ROOT
import uproot

import os

import numpy as np
import scipy as sp
import pandas as pd
import awkward as ak

import matplotlib.pyplot as plt

# specify path to filename
fileName = "samples/07-09-2021_58MB_Pt120_tune14_10k_SD/JetToyHIResultSoftDrop.root"
# print(os.getcwd()) # used to check your working directory

# obtain tree/branches from the file
file = uproot.open(fileName)
tree = file['jetTreeSig']
branches = tree.arrays()

data_set = branches[['sigJetRecur_dr12',
                     'sigJetRecur_jetpt',
                     'sigJetRecur_z']]
df_recur = ak.to_pandas(data_set)
df_recur


"""
pd.plotting.scatter_matrix(df_recur.head(10**4),
                           alpha=0.4,
                           hist_kwds={'bins': 50},
                           figsize=(7, 7))
plt.show()
"""
print("hoi")
flat_dr = ak.flatten(data_set["sigJetRecur_dr12"])[:10]
flat_kt = ak.flatten(data_set["sigJetRecur_jetpt"])[:10]

print(flat_dr, flat_kt)

plt.figure()
plt.plot(np.log(1/flat_dr),
         np.log(flat_kt))
plt.show()
