import scraper

if __name__ == "__main__":

    webscraper = scraper.Scraper()

    webscraper.open_website()

    for i in range(2, 81):
        webscraper.get_comment_author_date()
        webscraper.click_button_to_next_page(i)

    webscraper.zip_date_author_comment_together()

    webscraper.export_data_to_csv()

    webscraper.close_website()




