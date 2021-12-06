import csv, random
from collections import Counter


def load_donne_nutrition():
    csv_nutrition = open('Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv')
    nutrition = csv.DictReader(csv_nutrition)

    donnee_nutrition = []
    for element in nutrition:
        donnee_nutrition.append(element)

    return donnee_nutrition


def count_topic_nutrition(donnees):
    nbr = Counter()

    for i in donnees:
        nbr[i['Topic']] += 1
    return nbr


def filter_city_obesity(donnees):
    result = []

    for ligne in donnees:
        if ligne['Topic'] == 'Obesity / Weight Status':
            result.append(ligne)
    return result


def count_obesity_pro(donnees):
    nbr = Counter()
    donnees=filter_city_obesity(donnees)
    for i in donnees:
        nbr[i['LocationDesc']] += 1
    return nbr

def count_people_pro(donnees):
    nbr = Counter()

    for i in donnees:
        nbr[i['LocationDesc']] += 1
    return nbr


# Pro = dict()
# donnees=load_donne_nutrition()
# for i in donnees:
#     Pro[i['LocationDesc']]=i['LocationAbbr'].lower()

Province = {'ca':'California','tx':'Texas','oh':'Ohio','fl':'Florida','in':'Indiana','il':'Illinois','nc':'North California','ga':'Georgia','mo':'Missouri','ky':'Kentucky','va':'Virgina','pa':'Pennsylvania','ny':'New York','mi':'Michigan','tn':'Tennessee','sc':'South California','la':'Louisiana','al':'Alabama','wa':'Washington','ok':'Oklahoma','az':'Arizona','wi':'Wisconsin','ia':'Iowa','ut':'Utah','md':'Maryland','co':'Colorado','ar':'Arkansas','nj':'New Jersey','nm':'New Mexico','mn':'Minnesota','nv':'Nevada','ma':'Massachusetts','or':'Oregon','sd':'South Dakota','ks':'Kansas','id':'Idaho','ct':'Connecticut','wv':'West Virginia','ne':'Nebraska','ms':'Mississippi','nd':'North Dakota','me':'Maine','vt':'Vermont','wy':'Wyoming','hi':'Hawaii','nh':'New Hampshire','de':'Delaware','mt':'Montana','ri':'Rhode Island','dc':'District of Columbia','ak':'Alaska','co spgs':'Colorado','None':'None'}
