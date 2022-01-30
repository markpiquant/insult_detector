import Data.Insults
from textblob import TextBlob
import json
from process_tweet import tweetpropre
from Data.DictionnaireInsults import dicoef
import Data.DictionnaireInsults as dico
# Variables

# with open("Data/data.json") as json_data:
# d = json.load(json_data)

d_exemple = {
    "tweet_textual_content": {
        "0":
        "RT @StrayKidsGlobal: fuck shit",
        "1":
        "@TheSource \"Call Me Money\" is Live on all digital Platforms, Spotify link provided bellow, Go stream that Straight\u2026 https://t.co/rbtz9xD21E",
        "2":
        "RT @safemoon: #SAFEMOONARMY: don't miss @CptHodl 's keynote address at the @AIBCSummit in Malta this afternoon!\n\n\u23f0 8am PST / 11am EST / 4pm\u2026",
    },
    "ID": {
        "0": 1460971755120566282,
        "1": 1460971753824563208,
        "2": 1460971753543544838,
    },
    "ID_user": {
        "0": 1429508753016168453,
        "1": 2935534097,
        "2": 1288064942755794946,
    },
    "date": {
        "0": "Wednesday, 17. November 2021 02:03PM",
        "1": "Wednesday, 17. November 2021 02:03PM",
        "2": "Wednesday, 17. November 2021 02:03PM",
    },
    "Likes": {
        "0": 0,
        "1": 0,
        "2": 0,
    },
    "RTs": {
        "0": 331,
        "1": 0,
        "2": 433,
    },
    "hashtags": {
        "0": [],
        "1": [],
        "2": ["SAFEMOONARMY"],
    }
}

e = Data.Insults.insults

# Fonctions


def voc_data(dict):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par exemple d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        rs (Wordlist) : liste des mots contenus dans les tweets de dict (les tweets sont préalablement normalisés)
    """
    r = dict
    for keys in r["tweet_textual_content"]:
        r["tweet_textual_content"][keys] = tweetpropre(
            r["tweet_textual_content"][keys])
    a = r["tweet_textual_content"]
    z = TextBlob(str(a.values())[15::])
    s = z.words
    rs = s.lower()
    return rs


def voc_dataprime(dict):
    """
    Variante de voc_data
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par défaut d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        Lmots (list(WordList)) : liste de listes des mots contenus dans les tweets de dict (les tweets sont préalablement normalisés)
        Ltw (list(str)) : liste des tweets
        nb : les indices de Lmots et de Ltw correspondent. 
    Par exemple, Lmots[3] est une Wordlist des mots du 4ème tweet, dont le contenu normalisé est la string Ltw[3]
    """

    r = dict
    for keys in r["tweet_textual_content"]:
        r["tweet_textual_content"][keys] = tweetpropre(
            r["tweet_textual_content"][keys])
    a = r["tweet_textual_content"]
    Lmots = []
    Ltw = []
    for key in a:
        z = TextBlob(str(a[key]))
        s = z.words
        rs = s.lower()
        Lmots.append(rs)
        Ltw.append(a[key])
    return Lmots, Ltw


def insult_recoprime(dict):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par exemple d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        dico (dict) :
            clés : contenus textuels d'un tweet
            valeurs : listes des insultes contenues dans le tweet
    """
    r = dict
    dico = {}
    i = 0
    for tweet in voc_dataprime(dict)[0]:

        l = []
        for mot in tweet:
            if mot in e:
                l.append(mot)
        if l != []:
            dico[(voc_dataprime(dict)[1][i])] = l
        i += 1
    return dico


def nvx_dct(r):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par exemple d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        r (dict) : même dictionnaire dont les tweets ont été normalisés
    """

    for keys in r["tweet_textual_content"]:
        r["tweet_textual_content"][keys] = (tweetpropre(
            r["tweet_textual_content"][keys])).lower()
    return r


def insult_reco(dict):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par défaut d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        ret3 (tuple(str)) : insultes reconnues dans les tweets de dict

    fonction qui détecte les insultes parmis le jeu de tweet en entrée. Elle utilise la fonction voc_data qui rend l'ensemble des mots normalisés. 
    A partir de ces mots, la fonction reconnaît si des insultes sont présentent dans ces mots grâce à la base de données d'insulte appelée e que l'on a importé plus haut



    """
    s = voc_data(dict)
    ret = {}
    for word in s:
        c = 0
        if word in e:
            c += 1
        ret[word] = c
    ret2 = {}
    for word in ret:
        if ret[word] != 0:
            ret2[word] = ret[word]
    ret3 = tuple(ret2)

    return (ret3)


def tweet_insult(dict):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par défaut d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie :
        r (dict)

    fonction qui, grâce aux insultes détectées avec la fonction insult_reco, sélectionne les tweets contenant ces insultes dans le dict qui contient l'ensemble des tweets
    et les ressort dans un nouveau dictionnaire. 
    """
    a = insult_reco(dict)
    r = {}
    b = nvx_dct(dict)
    for keys in b["tweet_textual_content"]:
        for word in a:
            if word in b["tweet_textual_content"][keys]:
                r[keys] = b["tweet_textual_content"][keys]
    return r


def pourcentage_neg(dict):
    """
    Entrée : un dictionnaire de la même forme que les données importées depuis Twitter (par défaut d)
        clés : 'tweet_textual_content', 'ID', 'ID_user', 'date', 'Likes', 'RTs', 'hashtags'
    Sortie:
        r (dict) : clés = contenus textuels de tweets, valeurs = pourcentage d'insulte
    Prend le dictionnaire et sort les tweets où les insultes sont présentes en y ajoutant le %  d'insultes par tweets
    ce pourcentage est appelé négativité
    """
    r = {}

    a = tweet_insult(dict)

    for val in a.values():

        w = 0
        total = len(TextBlob(val).words)

        for word in TextBlob(val).words:
            if word in e:
                w += 1
        r[val] = w / total

    return r


def prop_neg(tweet):
    """
    Entrée : str (un tweet)
    Sortie : float entre 0 et 1 (nombre d'insultes/nombre de mots du tweet)
    """
    w = 0
    total = len(TextBlob(tweet).words)
    for word in TextBlob(tweet).words:
        if word in e:
            w += 1
    return w / total


def nb_insultes(tweet):
    """
    Entrée : str (un tweet)
    Sortie : int (nombre d'insultes du tweet)
    """
    w = 0
    for word in TextBlob(tweet).words:
        if word in e:
            w += 1
    return w


def coef_neg(dict):
    """
    Entrée : dict (un dictionnaire de tweets de la forme {"tweet":[liste des insultes contenues dans le tweet]})
    Sortie : dict (un dictionnaire de la forme {"tweet": pourcentage de négativité}
    """
    rr = {}
    c = dicoef
    for tweet in dict.keys():
        w = 0
        for ins in dict[tweet]:
            w += int(c[ins][0])*5
        rr[tweet] = w/len(TextBlob(tweet).words)
    return rr


# Instructions

if __name__ == '__main__':
    print(coef_neg(d))
