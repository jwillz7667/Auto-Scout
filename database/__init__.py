# database/__init__.py

import logging

from .db_connection import engine, metadata
from .models import cars

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Initialize database connection
    logger.info("Initializing database connection")
    # Add any initialization code if needed
except Exception as e:
    logger.error(f"Error initializing database: {e}")
    raise
