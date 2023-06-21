from bs_abgeorndete import Scraper

if __name__ == "__main__":
    scraper = Scraper()
    scraper.split_names_into_sur_and_last_name(Scraper.names)
    scraper.create_personal_email_adress(Scraper.surnames, Scraper.lastnames, Scraper.mailextension)
    scraper.load_data_into_dataframe(Scraper.surnames, Scraper.lastnames, Scraper.parties, Scraper.emails)
    scraper.export_to_excel(scraper.abgeordnete_df)