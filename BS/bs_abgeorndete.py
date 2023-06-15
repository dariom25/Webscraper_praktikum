from bs4 import BeautifulSoup
import requests

source = requests.get("https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Deutschen_Bundestages_(20._Wahlperiode)").text

soup = BeautifulSoup(source, "lxml")

tables = soup.find_all("table")

names = []
parties = []
email = []

counter = 0
for table in tables:
    counter += 1
    if counter == 3:
        politicians = table.find_all("tr")
        for person in politicians:
            data = person.find_all("td")
            scnd_counter = 0
            for entry in data:
                if scnd_counter == 1:
                    name = entry.text
                    name = name.strip("\n")   
                    names.append(name)
                elif scnd_counter == 3:
                    party = entry.text
                    parties.append(party)
                scnd_counter += 1

print(names)







