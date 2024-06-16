import os
import logging
from data_pipeline.extract import KBBAPI, CarScraper
from data_pipeline.transform import transform_car_data
from data_pipeline.load import load_data
from database.db_connection import engine
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    try:
        # Example of extracting data
        kbb_api = KBBAPI()
        models = kbb_api.get_models('toyota')
        if models:
            for model in models['results']:
                model_name = model['name']
                model_details = kbb_api.get_model_details('toyota', model_name)
                if model_details:
                    transformed_data = transform_car_data(model_details)
                    if transformed_data:
                        load_data(engine, transformed_data)
                    else:
                        logging.error(f"Error transforming data for model {model_name}")
                else:
                    logging.error(f"Error fetching details for model {model_name}")
        
        # Example of scraping data
        url = 'https://www.example.com/car-model-page'
        car_data = CarScraper.get_car_data(url)
        if car_data:
            transformed_data = transform_car_data(car_data)
            if transformed_data:
                load_data(engine, transformed_data)
            else:
                logging.error(f"Error transforming scraped data from {url}")
        else:
            logging.error(f"Error scraping data from {url}")
    except Exception as e:
        logging.error(f"An error occurred in the pipeline: {e}")
        raise

if __name__ == "__main__":
    run_pipeline()
