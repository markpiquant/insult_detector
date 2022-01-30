import json
import Data_collect.twitter_connection_setup as connect
import datetime


def collect(query, user, langue="en", nbr=10):
    '''
    Prend en argument une reqûete "query" et renvoie la liste des identifiants des tweets que renvoie la recherche.

    L'argument "user" désigne le compte developer twitter à utiliser.

    L'argument optionnel "langue" désigne la langue des tweets recherchés. Anglais par défaut.

    L'argument optionnel "nbr" désigne le nombre de tweets à renvoyer. 10 par défaut. 
    '''

    connexion = connect.twitter_setup(user)
    tweets = connexion.search_tweets(
        q=query,
        lang=langue,
        count=nbr,
    )
    L = []
    for tweet in tweets:
        L.append(tweet.id)
    return L


def store_tweets(tweets, filename, user):
    '''
    Stocke les informations des tweets dont les identifiants sont dans la liste "tweets".

    Les informations sont enregistrées dans le fichier filename du dossier Data/.
    filename est de la forme "Name_fichier.json"

    User pour choisir le compte developer twitter à utiliser
    Utilisez :"paul" ou "hugo" 
    '''

    connexion = connect.twitter_setup(user)
    directory = "Data/" + filename
    with open(directory) as json_data:
        Data = json.load(json_data)
    n = len(Data["ID"])
    for i in range(n, n + len(tweets)):
        status = connexion.get_status(tweets[i - n], tweet_mode="extended")
        Data["tweet_textual_content"][str(i)] = status.full_text
        Data["ID"][str(i)] = tweets[i - n]
        Data["ID_user"][str(i)] = status.user.id
        Data["date"][str(i)] = status.created_at.strftime(
            "%A, %d. %B %Y %I:%M%p")
        Data["Likes"][str(i)] = status.favorite_count
        Data["RTs"][str(i)] = status.retweet_count
        hashtags = []
        for dico in status.entities["hashtags"]:
            hashtags.append(dico["text"])
        Data["hashtags"][str(i)] = hashtags
    file = open(directory, "w")
    json.dump(Data, file)
    file.close()


def empty_data():
    '''
    Vide le contenu du fichier data.json 
    '''


file = open("Data/data.json", "w")
Data = {
    "tweet_textual_content": {},
    "ID": {},
    "ID_user": {},
    "date": {},
    "Likes": {},
    "RTs": {},
    "hashtags": {}
}
json.dump(Data, file)
file.close()


def request_store(query, filename, user="hugo", langue="en", nbr=10):
    '''
    Cette procédure rajoute au fichier "filename" du dossier Data les tweets renvoyés par la recherche "query"

    User pour choisir le compte developer twitter à utiliser (hugo par défaut).
    Utilisez "hugo" ou "paul".

    L'argument optionnel "langue" désigne la langue des tweets recherchés. Anglais par défaut.
    Utilisez : "fr" ou "en"  ou toutes autres langues en format ISO639-1.

    L'argument optionnel "nbr" désigne le nombre de tweets à renvoyer. 10 par défaut 
    '''

    l = collect(query, user, langue, nbr)
    store_tweets(l, filename, user)


# empty_data()
#request_store("Donald Trump","data.json",nbr=40)
