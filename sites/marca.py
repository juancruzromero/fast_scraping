# -*- coding: utf-8 -*-
from common import config

class Marca():
    def __init__(self, site, site_country):
        self.config = config()['sites'][site]
        self.site_country = site_country
        self.url = self.config['url']
        print(f"Starting \"{site}\" scraping...\n")

        self.scraping()

    def scraping(self):
        print("Write your code here!")