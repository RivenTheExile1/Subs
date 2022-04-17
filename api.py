from itertools import count

from setuptools import setup
import board


#checks to make sure all countries appear in their respective neighbors
def checker():
    countries = board.country_setup()
    for one_country in countries:
        neighbors = countries[one_country] 
        for one_neighbor in neighbors: 
            if one_neighbor not in countries:
                print(one_country, "Country x Neighbor y", one_neighbor, "is not a key")


#print all countries on the board       
def list_of_countries(): 
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)       
    print("Here is a list of countries in the world: ") 
    print(country_list)
     
#prints the boarders the country it has (idk how to word)
def boarders():
    country_we_want = input('What country do you wanna check the borders of: ')
    countries = board.country_setup()
    if country_we_want in countries:
        print(country_we_want, "boarders", countries[country_we_want])
    else:
        print("This isn't a country, check your spelling")
        boarders()


#list of fx()'s that print what countries are on what continent 
def north_american_countries():
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    na_countries = []
    for x in range(0,8):
        na_countries.append(country_list[x])
    
    print(na_countries)


def south_american_countries():
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    sa_countries = []
    for x in range(9,13):
        sa_countries.append(country_list[x])

    print(sa_countries)


def african_countries():
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    af_countries = []
    for x in range(13,19):
        af_countries.append(country_list[x])
    print(af_countries)


def oceania_countries(): 
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    oc_countries = []
    for x in range(19,23):
        oc_countries.append(country_list[x])
    print(oc_countries)

def european_countries():
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    eu_countries = []
    for x in range(23,30):
        eu_countries.append(country_list[x])
    print(eu_countries)

def asian_countries():
    countries = board.country_setup()
    country_list =[]
    for country in countries: 
        country_list.append(country)

    as_countries = []
    for x in range(30,42):
        as_countries.append(country_list[x])
    print(as_countries)









def allies():
    #will work on this late
    return None

def enemies():
    #opposite of allies
    return None


a = asian_countries()