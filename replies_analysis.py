import json
import Data_collect.twitter_connection_setup as connect
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import Data.Insults

connexion = connect.twitter_setup(user="hugo")

def get_replies_to_tweet(id_tweet, c=20, user="hugo", m=0, replies=[]):
    '''
    Cette fonction prend un tweet et renvoie les tweets réponses à ce tweet.

    Paramètres :
    id_tweet : identifiant du tweet
    c : donne le nombre de réponses à renvoyer
    m, replies : NE PAS UTILISER CES ARGUMENTS ! Ces arguments sont utilisés par la fonction lors d'appels récursifs

    Renvoie une List(int), contenant la liste des identifiants des réponses
    '''
    name = connexion.get_status(id_tweet).user.screen_name
    if m == 0:
        potential_replies = connexion.search_tweets(q='to:'+name, count=c)
    else:
        potential_replies = connexion.search_tweets(
            q='to:'+name, count=c, max_id=m)
    L = []
    for status in potential_replies:
        L.append(status.id)
        if status.in_reply_to_screen_name == name:
            replies.append(status.id)
    if len(replies) < c:
        if L ==[]:
            return []
        else:
            max = min(L)
            Message = ["Tqt ça arrive", "C'eeeeeest long", "Faut etre patient",
                    "Doucement le matin, pas trop vite le soir", "Plus qu'un instant ! ", "On y arrive", "ne t'endors pas", "youhou y'a quelqu'un ?"]
            n = np.random.randint(0, len(Message))
            print(Message[n])
            return get_replies_to_tweet(id_tweet, c, max, replies)
    else:
        return replies[0:c]

def prop_neg(tweet):
    """
    Entrée : str (un tweet)
    Sortie : float entre 0 et 1 (nombre d'insultes/nombre de mots du tweet)
    """
    e = Data.Insults.insults
    w = 0
    total = len(TextBlob(tweet).words)
    for word in TextBlob(tweet).words:
        if word in e:
            w += 1
    return w / total

def replies_avg_rate(id_tweet, nbr=10):
    '''
    Prend un tweet en renvoie le taux de négativité moyen des réponses à ce tweet.

    Arguments :
    - id_tweet (int) : identifiant du tweet
    - nbr = 10 (int) : nombre de réponses au tweet prises en compte

    Renvoie un float représentant le taux de négativité moyen des réponses
    '''
    replies = get_replies_to_tweet(id_tweet, c=nbr, user="hugo")
    n = len(replies)
    totalNeg = 0
    for id in replies:
        tweet = connexion.get_status(id).text
        neg = prop_neg(tweet)
        totalNeg += neg
    if n ==0:
        return -1
    else:
        return totalNeg/n


def trace_graphe(nbr=10):
    with open("Data/replies_analysis.json") as json_data:
        tweets = json.load(json_data)
    negs = []
    negs_replies = []
    for i in range(len(tweets["tweet_textual_content"])):
        neg = prop_neg(tweets["tweet_textual_content"][str(i)])
        neg_replies = replies_avg_rate(tweets["ID"][str(i)], nbr)
        negs.append(neg)
        negs_replies.append(neg_replies)
        print(negs, negs_replies)
    plt.plot(negs,negs_replies)
    plt.show()

trace_graphe(50)