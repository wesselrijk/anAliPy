import ROOT
import uproot

import pandas as pd
import numpy as np
import awkward as ak

# specify path to filename
fileName = "samples/07-09-2021_58MB_Pt120_tune14_10k_SD/JetToyHIResultSoftDrop.root"
# print(os.getcwd()) # used to check your working directory

# obtain tree/branches from the file
file = uproot.open(fileName)
tree = file["jetTreeSig"]
branches = tree.arrays()[
    ["sigJetRecur_dr12", "sigJetRecur_jetpt", "sigJetRecur_z"]
]  # 'branches' now stores the observables in 'awkward arrays'

# flatten
pts = branches["sigJetRecur_jetpt"]  # Awakward Array structure
pts_flat = ak.flatten(ak.flatten(pts))
print("Flatten test:", pts_flat, len(pts_flat), type(pts_flat), sep="\n")

# content of first 10 events
print(
    "\nFirst 10 events:",
    *(entry for entry in branches["sigJetRecur_dr12"][:10]),
    sep="\n"
)

# jets of the first event
print(
    "\nJets of first event:",
    *(jet for jet in branches["sigJetRecur_dr12"][0]),
    sep="\n"
)

# they work like numpy arrays and you can use numpy functions on them
print(
    "\nnp.exp(jet)", *(np.exp(jet) for jet in branches["sigJetRecur_dr12"][0]), sep="\n"
)

# from using numpy your array stays an awkward array
print(
    "\nCheck types: type before:",
    type(branches["sigJetRecur_dr12"][0]),
    "\ntype after:",
    type(np.log(branches["sigJetRecur_dr12"][0])),
)

# you cannot simply convert your jagged data to numpy
# print(type(ak.to_numpy(branches['sigJetRecur_dr12'][0]))) will give you an error!
# but individual jets will work
print(
    "type of a numpy converted jet:",
    type(ak.to_numpy(branches["sigJetRecur_dr12"][0, 1])),
)

# pandas example
df = ak.to_pandas(branches)
print(df.head())
print(df["sigJetRecur_dr12"][0, 0, 0])
