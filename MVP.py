import Data_collect.Collect as dc
import time
import Diagramme as c
import json
import reco_insulte as ri
import censure as css


def MVP(filename="data.json", user="hugo", langue="en"):
    """
    Entrées :
        filename (str) : le nom du fichier qui va contenir les données
        user (str) : le nom de l'utilisateur qui va extraire les tweets
        langue (str) : la langue des tweets extraits
        nbr (int) : le nombre de tweets qu'on importe à chaque itération
    Sorties : (selon les inputs)
        ins (tuple(str)) : le tuple des insultes contenues dans les tweets extraits
        twins (dict) : clé = contenu du tweet insultant, valeur (list(str)) = liste de la ou les insultes détectées dans le tweet
        neg (dict) : clé = contenu du tweet insultant, valeur (float) = taux de négativité du tweet, soit le nombre d'insultes sur le nombre de mots
        Affiche un diagramme de répartition des insultes par catégories
    """
    nb = int(input("\nHow many tweets ? "))
    query = str(input("\nEnter a key-word:"))
    dc.empty_data()
    print("Collecting Data...")
    time.sleep(1)
    print("\nError 404 : Not Found")
    time.sleep(1)
    print("It's a joke bro ;) it will work !")
    dc.request_store(query, filename, user="hugo", langue="en", nbr=nb)
    i = nb

    print("\nThere are "+str(i)+" tweets in data  ")

    A = str(input("Do you want to add tweets to data ? (y or n)\n"))

    while A == "y":
        print("Collecting Data...")
        dc.request_store(query, filename, user="hugo", langue="en", nbr=nb)
        i += nb
        print("\nThere are "+str(i)+" tweets in data")
        A = str(input("Do you want to add tweets to data ? (y or n)\n"))

    with open("Data/data.json") as json_data:
        dprime = json.load(json_data)
    print("Processing... Please wait")
    twins=ri.insult_recoprime(dprime)
    neg=ri.coef_neg(twins)
    ins=ri.insult_reco(dprime)
    
    A=int(input("\nAre you looking for:\nThe list of the insults ? Type 1\nThe tweets with insults ? Type 2\nThe rate of negativity of each tweet is ? Type 3\nThe censured tweets ? Type 4\nEach of these results ? Type 5\n"))
    if A==1:
        print(c.camembert(ins),c.diagramme(twins))
        
        return ins
    if A == 2:
        return twins
    if A == 3:
        return neg
    if A==4:
    
        return css.censure(twins)
    else:
        print("\n\nInsultes trouvées :\n")
        ch = ""
        for insulte in ins:
            ch += insulte + " ; "
        print(ch[0:-2])

        print("\n\nAnalyse des tweets :\n")
        for tweet in twins.keys():
            print("Tweet : {}".format(tweet))
            ch = ""
            for insult in twins[tweet]:
                ch += insult+" ; "
            print("Insults : {}".format(ch[0:-2]))
        print("\n\nTaux de négativité :\n")
        for tweet in neg.keys():
            print("\nTweet : {}".format(tweet))
            print("Rate of negativity : {}".format(str(neg[tweet])))

        print("\n\n\n Les tweets censurés sont :\n")
        for elt in css.censure(twins):
            print(elt)
            print('')
    print(c.camembert(ins),c.diagramme(twins))

if __name__ == '__main__':
    print(MVP())
