import matplotlib.pyplot as plt
import numpy as np
import Data.DictionnaireInsults as dico
from collections import Counter
import pylab

d=dico.dicoef



def camembert(listeinsultes):

    """
    fonction qui à partir d'une liste d'insultes génère un piechart montrant leur répartition selon leur caractère
    """

    Categories=[]
    for insult in listeinsultes:
        chaine=d[insult][1]
        for x in chaine.split("/"):
            Categories.append(x)   

    Count = Counter(Categories).most_common()
    Labels=[elt[0] for elt in Count]
    Occurence=np.array([elt[1] for elt in Count])

    plt.title("Répartition")
    plt.pie(Occurence, labels = Labels)
    plt.show() 

def diagramme(twins):
    """
    Génère un diagramme en barre représentant le nombre de fois qu'une insulte apparaît à 
    partir du dictionnaire twins {"tweet":[liste des insultes du tweet]}
    """
    fig = plt.figure()
    Listeinsulte=[]
    for elt in list(twins.values()):
        Listeinsulte+=elt
    Count = Counter(Listeinsulte).most_common()
    x=[i+1 for i in range(len(Count))]
    BarName=[elt[0] for elt in Count]
    height=[elt[1] for elt in Count]
    width = 0.5

    plt.bar(BarName, height)
    plt.show()
