import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import reco_insulte

d = reco_insulte.d

for k in d['tweet_textual_content']:
    d['prop_neg'] = {}
    d['nb_ins'] = {}
    d['prop_neg'][k] = reco_insulte.prop_neg(d['tweet_textual_content'][k])
    d['nb_ins'][k] = reco_insulte.nb_insultes(d['tweet_textual_content'][k])

df = pd.DataFrame(d)
"""
L'objectif de ce module est de représenter des graphiques sur les données des tweets, 
comme le graphe des RTs en fonction du nombre d'insultes par exemple.
"""


# exemples
def lin_reg():
    tips = sns.load_dataset("tips")
    g = sns.jointplot(x="total_bill",
                      y="tip",
                      data=tips,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 60),
                      ylim=(0, 12),
                      color="m",
                      height=7)
    plt.show()


def rt_likes():
    g = sns.jointplot(x="Likes",
                      y="RTs",
                      data=df,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 0.1),
                      ylim=(0, 7000),
                      color="m",
                      height=7)
    plt.show()


# Corrélations avec la proportion d'insultes
def rt_pn():
    g = sns.jointplot(x="prop_neg",
                      y="RTs",
                      data=df,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 0.1),
                      ylim=(0, 7000),
                      color="m",
                      height=7)
    plt.show()


def likes_pn():
    g = sns.jointplot(x="prop_neg",
                      y="Likes",
                      data=df,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 0.1),
                      ylim=(0, 7000),
                      color="m",
                      height=7)
    plt.show()


# Corrélations avec le nombre d'insultes


def rt_ni():
    g = sns.jointplot(x="nb_ins",
                      y="RTs",
                      data=df,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 10),
                      ylim=(0, 7000),
                      color="m",
                      height=7)
    plt.show()


def likes_ni():
    g = sns.jointplot(x="nb_ins",
                      y="Likes",
                      data=df,
                      kind="reg",
                      truncate=False,
                      xlim=(0, 10),
                      ylim=(0, 7000),
                      color="m",
                      height=7)
    plt.show()
