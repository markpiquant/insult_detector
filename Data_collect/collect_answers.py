import json
import Data_collect.twitter_connection_setup as connect
import datetime
import numpy as np
import time


def which_user(user="hugo"):
    return connect.twitter_setup(user)


connexion = which_user("noe")


def get_replies_to_tweet(id_tweet, c=20, m=0, replies=[], Lname=[], remember=0, type="mixed"):
    '''
    Cette fonction prend un tweet et renvoie les tweets réponses à ce tweet.

    Paramètres :
    id_tweet : identifiant du tweet
    c : donne le nombre de réponses à renvoyer
    m, replies : NE PAS UTILISER CES ARGUMENTS ! Ces arguments sont utilisés par la fonction lors d'appels récursifs

    Renvoie une List(int), contenant la liste des identifiants des réponses
    '''

    if c < 0:
        c = 0

    Lname.append(connexion.get_status(id_tweet).user.screen_name)
    if m == 0:
        query = 'to: '
        for i in range(len(Lname)-1, 0, -1):
            query += Lname[i] + ' '
        query += ' AND ' + Lname[0]
        potential_replies = connexion.search_tweets(
            q=query, count=c, result_type=type)
    else:
        query = 'to: '
        for i in range(len(Lname)-1, 0, -1):
            query += Lname[i] + ' '
        query += ' AND ' + Lname[0]
        potential_replies = connexion.search_tweets(
            q=query, count=c, result_type=type, max_id=m)
    L = []
    replies_remember = replies[::]
    for status in potential_replies:
        L.append(status.id)
        if status.in_reply_to_screen_name == Lname[-1]:
            replies.append(status.id)
    if len(replies) < c and remember < 10 and L != []:
        if len(replies_remember) == len(replies):
            remember += 1
        else:
            remember = 0
        max = min(L)
        Message = [
            "Tqt ça arrive", "C'eeeeeest long", "Faut etre patient",
            "Doucement le matin, pas trop vite le soir",
            "Plus qu'un instant ! ", "On y arrive", "ne t'endors pas",
            "youhou y'a quelqu'un ?"
        ]
        n = np.random.randint(0, len(Message))
        print(Message[n])
        return get_replies_to_tweet(id_tweet, c, max, replies, remember=remember, type=type)
    else:
        return list(set(replies[0:c]))


'''
# C'est un test
replies = get_replies_to_tweet(1460810034913361921) 
connexion = connect.twitter_setup()
for id in replies:
    text = connexion.get_status(id).text
    print("Id : {} \n Text : {}".format(id, text))
'''


def replies_inception(id_tweet, noeud, c=20, m=0, inception={}, Lname=[], historic=[], type="mixed"):
    inception = {"Response": {}, "text": connexion.get_status(
        id_tweet, tweet_mode="extended").full_text}
    if noeud == 0:
        return inception
    else:
        historic.append(id_tweet)
        Replies = get_replies_to_tweet(id_tweet, c, m, type=type)
        print(Replies)
        if Replies == []:
            print("Resplies est vide")
            return inception
        else:
            for r in Replies:
                if r not in historic:
                    historic.append(r)
                    Lname.append(connexion.get_status(
                        id_tweet).user.screen_name)
                    print(Lname)
                    inception["Response"][str(r)] = {}
                    inception["Response"][str(r)] = replies_inception(
                        r, noeud-1, 2, m, inception["Response"][str(r)], Lname, historic, type)
                    Lname = []
        return inception


def create_json(file_name, id_tweet, noeud, c=20, type="mixed"):
    dico = replies_inception(id_tweet, noeud, c, type=type)
    True_file_name = "Data/"+file_name+".json"
    file = open(True_file_name, "w")
    json.dump(dico, file)
    file.close()


#create_json("data_rep_Bernie", 1461086492835651586, 3)


#print(replies_inception(1461153182529294338, noeud=3, c=2, inception={}))
#print(get_replies_to_tweet(1461245049585426435, c=5))
