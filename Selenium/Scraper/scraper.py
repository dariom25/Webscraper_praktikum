from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


class Scraper:
    website_link = "https://forum.gamespodcast.de/viewtopic.php?f=2&t=9368"
    header = ["date", "time", "author", "comment"]

    def __init__(self, comments=None, author=None, date=None, time=None):
        self.driver = webdriver.Firefox()
        self.comments = comments
        if self.comments == None:
            self.comments = []
        self.author = author
        if self.author == None:
            self.author = []
        self.date = date
        if self.date == None:
            self.date = []
        self.d_a_c_list = []
        self.time = time
        if self.time == None:
            self.time = []
        self.d_a_c_list = []

    def open_website(self):
        self.driver.get(Scraper.website_link)

    def close_website(self):
        self.driver.quit()

    def print_title(self):
        print(self.driver.title)

    def get_comment_author_date(self):
        """gets the comment, the author and the date by their-id number
        id: string"""
        page_body = self.driver.find_elements(By.ID, "page-body")
        for post in page_body:
            postbody = post.find_elements(By.CLASS_NAME, "content")
            for element in postbody:
                new_element = element.text.replace("↑\n", " ")
                new_element = element.text.replace("\n", " ")
                self.comments.append(str(new_element))
            author = post.find_elements(By.CLASS_NAME, "username")
            for name in author:
                self.author.append(str(name.text))

            date = post.find_elements(By.TAG_NAME, "time")
            for day in date:
                date_and_time = day.text.split(", ")
                self.date.append(date_and_time[0])
                self.time.append(date_and_time[1])


    def zip_date_author_comment_together(self):
        self.d_a_c_list = list(zip(self.date, self.time, self.author, self.comments))

    def export_data_to_csv(self):
        with open("date_author_comment_csv.csv", "w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            csv_writer.writerow(self.header)
            for data in self.d_a_c_list:
                csv_writer.writerow(data)
                print(data)

    def click_button_to_next_page(self, number_of_page):
        """clicks a button to change to the next page
        """
        next_page = self.driver.find_element(By.LINK_TEXT, str(number_of_page))
        next_page.click()

