from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

class Scraper:
    website_link = "https://www.bundestag.de/abgeordnete"
    header = ["Name", "Vorname", "Email", "Partei"]
    
    def __init__(self, name=None, surname=None, email=None, party=None):
        self.driver = webdriver.Firefox()
        self.name = name
        if self.name == None:
            self.name = []
        self.surname = surname 
        if self.surname == None:
            self.surname = []
        self.email = email
        if self.email == None:
            self.email = []
        self.party = party  
        if self.party == None:
            self.party = []
        self.name_surname_email_party = []
    
    def open_website(self):
        """Opens the website
        """
        self.driver.get(Scraper.website_link)
    
    def close_website(self):
        self.driver.quit()
        
    def click_button_to_continue(self):
        next_page = self.driver.find_element(By.CSS_SELECTOR, "slick-next.slick-arrwo")
        next_page.clear()
    
    def get_party(self):
        party = self.driver.find_element(By.CLASS_NAME, "bt-person-fraktion")
        self.party.append(str(party))
    
    #timer einbauen
    #größeres element wählen
    #anderes element testen
    #andere tutorials gucken

if __name__ == "__main__":
    scraper = Scraper()
    scraper.open_website()
    scraper.get_party()
    print(scraper.party)