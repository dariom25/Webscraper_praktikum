from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


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
        self.replace_special_characters_in_surnames("ö", "oe", surnames)
        self.replace_special_characters_in_surnames("ü", "ue", self.edited_surnames)
        self.replace_special_characters_in_surnames("ä", "ae", self.edited_surnames)
        self.replace_special_characters_in_surnames("é", "e", self.edited_surnames)        
        self.replace_special_characters_in_surnames("ğ", "g", self.edited_surnames)
        self.replace_special_characters_in_surnames("ó", "o", self.edited_surnames)
        self.replace_special_characters_in_surnames("ò", "o", self.edited_surnames)
        self.replace_special_characters_in_surnames("ß", "ss", self.edited_surnames)
        self.replace_special_characters_in_surnames("ă", "a", self.edited_surnames)
        self.replace_special_characters_in_surnames("č", "c", self.edited_surnames)
        self.replace_special_characters_in_surnames("ç", "c", self.edited_surnames)
        
        self.replace_special_characters_in_lastnames("ö", "oe", lastnames)
        self.replace_special_characters_in_lastnames("ü", "ue", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ä", "ae", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("é", "e", self.edited_lastnames)        
        self.replace_special_characters_in_lastnames("ğ", "g", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ó", "o", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ò", "o", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ß", "ss", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ă", "a", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("č", "c", self.edited_lastnames)
        self.replace_special_characters_in_lastnames("ç", "c", self.edited_lastnames)


        for surname, lastname in zip(self.edited_surnames, self.edited_lastnames): # irgendwie will er hier keine mailadressen draus machen --> debugger
            email = surname.lower() + "." + lastname.lower() + mailextension

            Scraper.emails.append(email)
    
    def replace_special_characters_in_surnames(self, character, replacement, names):
        self.edited_surnames = []
        for name in names:
            edited_name = name.replace(character, replacement)
            self.edited_surnames.append(edited_name)
        return self.edited_surnames
    
    def replace_special_characters_in_lastnames(self, character, replacement, names):
        self.edited_lastnames = []
        for name in names:
            edited_name = name.replace(character, replacement)
            self.edited_lastnames.append(edited_name)
        return self.edited_lastnames

    
    def load_data_into_dataframe(self, surname, lastname, party, email):
        pass
        
# TODO: Sonderfälle: Umlaute (ö,ä,ü); doppelnamen; Sonderzeichen; ß / ss;  
# TODO: Anzupassen: Doppelte Vornamen und Nachnahmen --> richtig getrennt? Mail korrekt?
# doppelte nachnamen mit bindestrich werden normal in die mailadresse aufgenommen
# doppelte nachnahme ohne bindestrich werden zusammengeschrieben (de ridder -> deridder)
# doppelte vornamen mit bindestrich, kommen mit bindestrich in mail (hans-peter)
# ß zu ss

if __name__ == "__main__":
    scraper = Scraper()
    scraper.split_names_into_sur_and_last_name(Scraper.names)
    scraper.create_personal_email_adress(Scraper.surnames, Scraper.lastnames, Scraper.mailextension)
    print(scraper.emails) 
    




