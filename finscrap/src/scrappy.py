import requests
import pandas as pd
from bs4 import BeautifulSoup

references_tag = {
    
}

class Scrappy:
    def __init__(self, url):
        self.url = url
        self.data = None
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'Cache-Control': 'max-age=0',
                        'Referer': 'https://www.google.com/' }

    def fetch_data(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.data = response.text
        else:
            raise Exception(f"Failed to fetch data from {self.url}")

    def parse_data(self):
        if not self.data:
            raise Exception("No data to parse. Please fetch data first.")
        
        soup = BeautifulSoup(self.data, 'html.parser')
        # Example parsing logic (to be customized based on actual HTML structure)
        
        return pd.DataFrame(soup)

def main():
    url = "https://fr.finance.yahoo.com/"  # Replace with actual URL
    scrappy = Scrappy(url)
    
    try:
        scrappy.fetch_data()
        parsed_data = scrappy.parse_data()
        print(parsed_data.head())
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()