from bs4 import BeautifulSoup
import requests



names = []
parties = []
email = []

def parse_name_and_party_from_html_code():
    
    source = requests.get("https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Deutschen_Bundestages_(20._Wahlperiode)").text

    soup = BeautifulSoup(source, "lxml")

    tables = soup.find_all("table")
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
                        party = party.strip("\n")
                        parties.append(party)
                    scnd_counter += 1

def export_data_to_txt(parties, names):
    with open("bundestagsparteien.txt", "w", encoding="UTF-8") as f:
        f.write("Partei" + "\n")
        for partei in parties:
            f.write(partei + ",\n")

    with open("bundestagsabgeordnete.txt", "w", encoding="UTF-8") as f:
        f.write("Name" + "\n")
        for name in names:
            f.write(name + ",\n")







