import pytest
import logging
from data_pipeline.extract import KBBAPI, CarScraper

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def kbb_api():
    return KBBAPI()

@pytest.fixture
def car_scraper():
    return CarScraper()

def test_kbb_api_get_models(kbb_api):
    try:
        response = kbb_api.get_models('toyota')
        assert response is not None
        assert 'results' in response
    except Exception as e:
        logging.error(f"An error occurred during test_kbb_api_get_models: {e}")
        pytest.fail(f"test_kbb_api_get_models failed due to an exception: {e}")

def test_kbb_api_get_model_details(kbb_api):
    try:
        response = kbb_api.get_model_details('toyota', 'camry')
        assert response is not None
        assert 'name' in response
    except Exception as e:
        logging.error(f"An error occurred during test_kbb_api_get_model_details: {e}")
        pytest.fail(f"test_kbb_api_get_model_details failed due to an exception: {e}")

def test_car_scraper_get_car_data(car_scraper):
    url = 'https://www.example.com/car-model-page'
    try:
        response = car_scraper.get_car_data(url)
        assert response is not None
        assert 'model' in response
        assert 'price' in response
    except Exception as e:
        logging.error(f"An error occurred during test_car_scraper_get_car_data: {e}")
        pytest.fail(f"test_car_scraper_get_car_data failed due to an exception: {e}")
