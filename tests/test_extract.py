import pytest
from data_pipeline.extract import KBBAPI, CarScraper

@pytest.fixture
def kbb_api():
    return KBBAPI()

@pytest.fixture
def car_scraper():
    return CarScraper()

def test_kbb_api_get_models(kbb_api):
    response = kbb_api.get_models('toyota')
    assert response is not None
    assert 'results' in response

def test_kbb_api_get_model_details(kbb_api):
    response = kbb_api.get_model_details('toyota', 'camry')
    assert response is not None
    assert 'name' in response

def test_car_scraper_get_car_data(car_scraper):
    url = 'https://www.example.com/car-model-page'
    response = car_scraper.get_car_data(url)
    assert response is not None
    assert 'model' in response
    assert 'price' in response
