class HtmlDownloader():

    def __init__(self) -> None:
        self.url    = None
        self.html   = None

    def set_url(self, url : str) -> None:
        self.url = url

    def get_url(self) -> str:
        self.url

    def load(self) -> None:
        pass