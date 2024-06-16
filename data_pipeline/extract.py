import requests
from bs4 import BeautifulSoup
import logging
from .config import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class KBBAPI:
    BASE_URL = 'https://api.kbb.com'
    API_KEY = config.KBB_API_KEY

    @staticmethod
    def get_models(make):
        try:
            endpoint = f'{KBBAPI.BASE_URL}/api/v2/vehicles?make={make}&apikey={KBBAPI.API_KEY}'
            response = requests.get(endpoint)
            response.raise_for_status()  # Ensure we notice bad responses
            logging.info(f"Successfully fetched models for {make}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching models for {make}: {e}")
            return None

    @staticmethod
    def get_model_details(make, model):
        try:
            endpoint = f'{KBBAPI.BASE_URL}/api/v2/vehicles/{make}/{model}?apikey={KBBAPI.API_KEY}'
            response = requests.get(endpoint)
            response.raise_for_status()  # Ensure we notice bad responses
            logging.info(f"Successfully fetched details for {make} {model}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching details for {make} {model}: {e}")
            return None

class CarScraper:
    @staticmethod
    def get_car_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure we notice bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            car_model = soup.find('h1', {'class': 'car-model'}).text
            car_price = soup.find('span', {'class': 'car-price'}).text
            logging.info(f"Successfully scraped data from {url}")
            return {'model': car_model, 'price': car_price}
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from {url}: {e}")
            return None
        except AttributeError as e:
            logging.error(f"Error parsing data from {url}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    kbb_api = KBBAPI()
    models = kbb_api.get_models('toyota')
    print(models)
    model_details = kbb_api.get_model_details('toyota', 'camry')
    print(model_details)

    url = 'https://www.example.com/car-model-page'
    car_data = CarScraper.get_car_data(url)
    print(car_data)
