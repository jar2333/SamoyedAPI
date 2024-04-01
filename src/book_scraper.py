from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from cachetools import cached, TTLCache

class BookScraper:
    def __init__(self, url: str):
        self.url = url

    @cached(cache=TTLCache(maxsize=1, ttl=86400))
    def scrape(self) -> List[Dict[str, str]]:
        html = self.request()
        responses = self.parse(html)

        return responses    

    def request(self) -> str:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except Exception as err:
            raise err
        else:
            return response.text
            
    def parse(self, html: str) -> List[Dict[str, str]]:
        # Find parent element
        soup = BeautifulSoup(html, "lxml")

        root = soup.find(id="currentlyReadingReviews")

        # Iterate through children
        out = []
        for child in root.children:
            if isinstance(child, str) or child["class"] == "clear":
                continue

            # Get first column tags
            c1 = soup.select_one("div.firstcol")

            image_tag = c1.img

            # Get second column tags
            c2 = soup.select_one("div.secondcol")

            info_tag = c2.select_one("div.whos-review")

            title_tag = info_tag.select_one("a.bookTitle")
            author_tag = info_tag.select_one("a.authorName")

            progress_tag = c2.div.findNextSibling("div").a


            # Get fields
            title = title_tag.text
            url = "http://goodreads.com" + title_tag["href"]

            author = author_tag.text
            author_url = "http://goodreads.com" + author_tag["href"]

            image_url = image_tag["src"]

            progress_percent = progress_tag.text.strip("()%")
            assert progress_percent.isdigit()

            # Output parsed data
            out.append({
                "title": title,
                "url": url,
                "author": author,
                "author_url": author_url,
                "image_url": image_url,
                "progress": progress_percent
            })

        return out







