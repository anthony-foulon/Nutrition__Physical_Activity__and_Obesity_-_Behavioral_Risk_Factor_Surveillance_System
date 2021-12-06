import csv
from collections import Counter
import itertools
from Projet2_complement import *

def load_donne_Fastfood():
    FastFoodRestaurants = open('FastFoodRestaurants.csv')
    FastFood = csv.DictReader(FastFoodRestaurants)
    # return FastFood
    donnee_Fastfood = []
    for fastfood in FastFood:
        donnee_Fastfood.append(fastfood)

    return donnee_Fastfood

def count_fastFood(donnees):
    nbr_fastFood = Counter()
    for i in donnees:
        nbr_fastFood[i['name'].lower()] += 1

    return nbr_fastFood

def count_ff_province(donnees):
    nbr_ff = Counter()
    ff_city = dict()                    #compte nombre fastfood par province
    for i in donnees:
        nbr_ff[i['province'].lower()] += 1

    return nbr_ff


def top_ten_fastFood(donnees):
    donnees = count_fastFood(donnees)
    top_ten = donnees.most_common()[:10]

    return top_ten

if __name__ == '__main__':
    FastFood = load_donne_Fastfood()
    Nutrition = load_donne_nutrition()
    ff_city = count_ff_province(FastFood)

    people_pro=count_people_pro(Nutrition)
    people_obesity_pro=count_obesity_pro(Nutrition)


    nbr_FF=dict()
    for (province, nbr_ff) in ff_city.most_common():
        province = Province[province]
        nbr_FF[province] = nbr_ff
    

    print('Province','-', 'Nombre de personne','-', 'Nombre de personne atteinte d\'obésité','-','Nombre de FastFood')
    for (province, nbr_personne) in people_pro.most_common():
        if province in nbr_FF:
            print(province,'-', nbr_personne,'-', people_obesity_pro[province],'-',nbr_FF[province])
        else:
            print(province,'-', nbr_personne,'-', people_obesity_pro[province],'-','Pas d\'informations')

    # print('Province', 'Nombre de FastFood')
    # for (province, nbr_ff) in ff_city.most_common():
    #     print(province, nbr_ff)
