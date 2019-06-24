# Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером.


class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
