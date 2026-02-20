import requests
from urllib.parse import urljoin

class SatisfactoryCalculator:
    """
    Client to interact with satisfactorycalculator.com
    """
    
    def __init__(self):
        self.base_url = "https://satisfactorycalculator.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_page(self, path=""):
        """Fetch a page from the calculator"""
        url = urljoin(self.base_url, path)
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def fetch_home(self):
        """Fetch the homepage"""
        return self.get_page("/")
    
    def fetch_data(self, endpoint):
        """Fetch data from a specific endpoint"""
        return self.get_page(f"/{endpoint}")

if __name__ == "__main__":
    calculator = SatisfactoryCalculator()
    print("Connecting to satisfactorycalculator.com...")
    home_data = calculator.fetch_home()
    if home_data:
        print("✓ Successfully connected!")
        print(f"Received {len(home_data)} bytes of data")
    else:
        print("✗ Failed to connect")