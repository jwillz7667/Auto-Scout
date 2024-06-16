# data_pipeline/__init__.py

import logging

from .extract import KBBAPI, CarScraper
from .transform import transform_car_data
from .load import load_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Initialize data pipeline
    logger.info("Initializing data pipeline")
    # Add any initialization code if needed
except Exception as e:
    logger.error(f"Error initializing data pipeline: {e}")
    raise
