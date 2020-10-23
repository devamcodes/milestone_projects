from bs4 import BeautifulSoup

from locators.qoutes_page_locators import QuotePageLocators
from parsers.qoute import QuoteParser

class QuotesPage:
    def __init__(self):
        self.soup = BeautifulSoup(page, 'html.parser')


    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]