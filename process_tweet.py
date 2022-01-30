import textblob
import json
from textblob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier

'''
Tests :
wiki = "I was enjoying eating apples. She is no longer loved"
testfr = "J'aime manger les pommes de mon jardin"
tweettest = "RT @Sifaoui: 1\ufe0f\u20e3In their translation of @EmmanuelMacron's speeches, the @AlJazeera propagandists knowingly made the French president say \u201cI\u2026"
blob = TextBlob("Comment vas-tu?")
'''

with open('StopWord/stop_words_english.json', encoding="utf8") as mon_fichier:
    stop_words_en = json.load(mon_fichier)

with open('StopWord/stop_words_french.json', encoding="utf8") as mon_fichier:
    stop_words_fr = json.load(mon_fichier)


def filtreCaracteres(text):
    """
    entrée : text (str)
    sortie : lp (str)
    Retire les caractères spéciaux d'un texte (format string) tels que les emojis
    """

    l = list(text)
    lp = ""
    for x in l:
        if ord('x') <= 55295:
            lp += x
    return lp


def retireHttp(text):
    """
    entrée : text (str)
    sortie : (str)
    Retire les liens http d'un texte (format string)
    """
    l = text.split(" ")
    resultat = ""
    for mot in l:
        isHttp = mot[0:5] == "http:" or mot[0:6] == "https:"
        if not isHttp:
            resultat += mot + " "
    return resultat[:-1]


def retireAt(text):
    """
    entrée : text (str)
    sortie : (str)
    Retire les arobases
    """
    return text.replace("@", "")


def retireRetourLigne(text):
    """
    entrée : text (str)
    sortie : (str)
    Retire les retours à la ligne
    """
    return text.replace("\n", "")


def lemmatizeSentence(text):
    """
    entrée : text (str)
    sortie : (str)
    Lemmatize une phrase et renvoie la chaine de caractere "propre" (text=une phrase)
    """
    wordTag = text.tags
    l = ""
    for (mot, tag) in wordTag:
        motLemmatise = ""
        if tag[0] != 'V':
            motLemmatise = Word(mot).lemmatize()
        else:
            motLemmatise = Word(mot).lemmatize()
        if motLemmatise not in []:
            l += motLemmatise + " "
    return l[:-1]


def trilangueepuration(tweetcomplexe):
    """
    entrée : text (str)
    sortie : S (str)
    Prends une chaîne de caracteres privée d'émojis/liens ... et renvoie le tweet lematizé
    """
    tweet = TextBlob(tweetcomplexe)

    S = ""
    for phrase in tweet.sentences:
        S += " " + lemmatizeSentence(phrase) + "."
    return S


def tweetpropre(tweetbrut):
    """
    entrée : tweetbrut (str)
    sortie : (str)
    prend en parametre un tweet brut et retourne une chaine de caractere lemmatize
    (composée de filtreCaracteres, retireAt, retireHttp, retireRetourLigne, trilangueepuration)
    """
    tweetsanscarac = retireAt(filtreCaracteres(tweetbrut))
    tweetsanscarachttp = retireHttp(tweetsanscarac)
    twsanscarhttpligne = retireRetourLigne(tweetsanscarachttp)
    return trilangueepuration(twsanscarhttpligne)
