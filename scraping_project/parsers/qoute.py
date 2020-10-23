from locators.qoute_locators import Quotelocartors

class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'(Quote {self.content}, by {self.author}'


    @property
    def content(self):
        locator = Quotelocartors.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = Quotelocartors.AUTHOR
        return self.parent.select_one(locator).string


    @property
    def tags(self):
        locator = Quotelocartors.TAGS
        return [e.string for e in self.parent.select(locator)]