from bs4 import BeautifulSoup
import requests
import pandas as pd


class Scraper:
    names = []
    parties = []
    emails = []
    surnames = []
    lastnames= []
    mailextension = "@bundestag.de"

    def __init__(self):
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
                            Scraper.names.append(name)
                        elif scnd_counter == 3:
                            party = entry.text
                            party = party.strip("\n")
                            Scraper.parties.append(party)
                        scnd_counter += 1

    def export_parties_to_txt(self, parties):
        with open("bundestagsparteien.txt", "w", encoding="UTF-8") as f:
            f.write("Partei" + "\n")
            for partei in parties:
                f.write(partei + ",\n")

    def export_names_to_txt(self, names):
        with open("bundestagsabgeordnete.txt", "w", encoding="UTF-8") as f:
            f.write("Name" + "\n")
            for name in names:
                f.write(name + ",\n")
    
    def split_names_into_sur_and_last_name(self, names):
        for name in names:
            surname, lastname = name.split(" ", 1)
            Scraper.surnames.append(surname)
            Scraper.lastnames.append(lastname)
    
    def create_personal_email_adress(self, surnames, lastnames, mailextension):
        for surname, lastname in zip(surnames, lastnames):
            email = surname.lower() + "." + lastname.lower() + mailextension
            print(email)
    
    def load_data_into_dataframe(self, surname, lastname, party, email):
        pass
        

if __name__ == "__main__":
    scraper = Scraper()
    scraper.split_names_into_sur_and_last_name(Scraper.names)
    scraper.create_personal_email_adress(Scraper.surnames, Scraper.lastnames, Scraper.mailextension)




