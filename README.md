# insult_detector
Training an insultes detector for tweets
# CSA (CentraleSupélec Autocensure)


# Sommaire
- [Description](#description)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributors](#contributors)

# Description
[Haut](#sommaire)

Insult detector in a tweet (MVP).

Evaluation of each tweet vulgarity :
* Each word will be attributed a coefficient of rudeness on a 1 to 5 scale. Thus, or each tweet, we can create a rudeness factor indicating a vulgarity level.

Censorship : 
* Censoring insults when detected

Analyse of a topic.
* Graphical representation of insultes and their categories on a given topic. 

Evaluation of the hate wave linked linked with the topic : 
* Regression evaluation of the link between the tweet rudeness and its RTs rudeness. 

# Installation
[Top](#summary)

Clone the repoository (with the following bash command `git clone https://gitlab-ovh-02.cloud.centralesupelec.fr/paul.salquebre/csa.git`)

Install the necessary packages : 
+ numpy
+ seaborn
+ matplotlib
+ pandas
+ TextBlob
+ Json
+ Tweepy

# Utilisation
[Top](#summary)

fill in the file Credentials_Hugo your API twitter keys (You can get them freely on Twitter's website).
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY =
CONSUMER_SECRET = 

BEARER_KEY =

# Access:
ACCESS_TOKEN = 
ACCESS_SECRET = 


Exécute MVP.py with the folowing bash command `python MVP.py`

Then answer these questions in the terminal :
* topic
* number of tweet treated
* results template wished

# Contributors
[Haut](#sommaire)

* Marius Nahon
* Paul Salquebre
* Hugo Hakem
* Mark Piquant
* Noé Prat
