import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")
dead = data["Treatment Outcome"] 
tp53 = data ["TP53 (aka p53) genotype"]
one_hot = pd.get_dummies(tp53)
#print(one_hot["pathogenic mutant"].value_counts())

withtp53 = data.loc[data["TP53 (aka p53) genotype"] == "pathogenic mutant", "Treatment Outcome"]
print(withtp53)
newone_hot = pd.get_dummies(withtp53)
print(newone_hot)
print(newone_hot["Deceased"].value_counts())

owithtp53 = data.loc[data["TP53 (aka p53) genotype"] == "wild-type", "Treatment Outcome"]
print(owithtp53)
anewone_hot = pd.get_dummies(owithtp53)
print(anewone_hot)
print(anewone_hot["Deceased"].value_counts())
