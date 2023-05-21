import requests
import time
#Send message

ids = []

def getData():
    file = open('data.txt', 'w')
    for x in range(11000, 16000):
        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(x)

        response = requests.get(url)
        data = response.json()

        if data['drinks'] != None:
            nombre = data['drinks'][0]['strDrink']
            #-- Guardar data
            print(nombre)
            file.write(nombre +'\n')


getData()

