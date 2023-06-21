from bs_abgeorndete import Scraper

if __name__ == "__main__":
    scraper = Scraper()
    scraper.load_data_from_excel("BS/Abgeordnete_Landtag_NRW_noch_ohne_Mail.xlsx")
    scraper.select_column()
    scraper.split_names_into_sur_and_last_name(scraper.names)
    scraper.create_personal_email_adress(Scraper.surnames, Scraper.lastnames, Scraper.mailextension)
    scraper.add_party_to_a_list()
    scraper.load_data_into_dataframe(Scraper.surnames, Scraper.lastnames, Scraper.parties, Scraper.emails)
    scraper.export_to_excel(scraper.abgeordnete_df, "Abgeordnete_NRW.xlsx")