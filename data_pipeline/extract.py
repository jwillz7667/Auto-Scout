import requests
from bs4 import BeautifulSoup
import logging
from .config import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class KBBAPI:
    """
    Class to interact with the Kelley Blue Book API.
    """
    BASE_URL = 'https://api.kbb.com'
    API_KEY = config.KBB_API_KEY

    @staticmethod
    def get_models(make):
        """
        Get models for a given make from the KBB API.

        :param make: Car make (e.g., 'toyota').
        :return: JSON response with models or None if an error occurs.
        """
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
        """
        Get details for a given make and model from the KBB API.

        :param make: Car make (e.g., 'toyota').
        :param model: Car model (e.g., 'camry').
        :return: JSON response with model details or None if an error occurs.
        """
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
    """
    Class to scrape car data from a given URL.
    """
    @staticmethod
    def get_car_data(url):
        """
        Get car data from a given URL.

        :param url: URL of the car model page.
        :return: Dictionary with car model and price or None if an error occurs.
        """
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
