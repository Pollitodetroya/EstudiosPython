from bs4 import BeautifulSoup
import requests
import time
# link pagina:
url = "https://us.as.com/resultados/futbol/italia/clasificacion/"
page = requests.get(url) # Optenemos la pagina
soup = BeautifulSoup(page.content,'html.parser')
prueba = soup.find_all("span", class_="nombre-equipo")
equipos = list()
count = 0
for i in prueba:
    if count == 20:
        break
    count +=1
    equipos.append(i.text) # Cogemos solo el texto de la etiqueta span
for i in range(0,20):
    print("puesto: %d equipo: %s" % (i+1, equipos[i]))