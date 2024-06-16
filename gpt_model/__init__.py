# gpt_model/__init__.py

import logging

from .fine_tune import fine_tune_model
from .generate_responses import generate_response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Initialize GPT model
    logger.info("Initializing GPT model")
    # Add any initialization code if needed
except Exception as e:
    logger.error(f"Error initializing GPT model: {e}")
    raise
