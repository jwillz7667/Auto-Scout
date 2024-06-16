# tests/__init__.py

# This can be left empty or used to import test modules
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from .test_extract import TestKBBAPI, TestCarScraper
from .test_transform import TestTransformCarData
from .test_load import TestLoadData
from .test_gpt_model import TestFineTuneModel, TestGenerateResponse
