from typing import List, Dict
import requests
from bs4 import BeautifulSoup

class BookScraper:
    """
    Scrapes the available book data at the given url.
    """
    
    def __init__(self, url: str):
        assert url is not None
        self.url = url

    def scrape(self) -> List[Dict[str, str]]:
        html = self.request()
        responses = self.parse(html)

        return responses    

    def request(self) -> str:
        try:
            response = requests.get(self.url, headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US',
                'Connection': 'keep-alive',
                'Host': 'www.goodreads.com',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
            })
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
        for child in root.select("div.Updates"):
            assert child.name == "div"

            # Get first column tags
            c1 = child.select_one("div.firstcol")

            image_tag = c1.img

            # Get second column tags
            c2 = child.select_one("div.secondcol")

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

            # Extract progress percentage
            progress_text = progress_tag.text.strip("()%")
            if progress_text.startswith("page"):
                split = progress_text.split()
                current = int(split[1])
                total = int(split[-1])
                progress_percent = (100*current)//total
            else:
                progress_percent = int(progress_text)
            
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







