from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, JSON, TIMESTAMP
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import logging
from .config import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATABASE_URI = config.DATABASE_URI
engine = create_engine(DATABASE_URI)
metadata = MetaData()

cars = Table('cars', metadata,
             Column('id', Integer, primary_key=True),
             Column('make', String),
             Column('model', String),
             Column('year', Integer),
             Column('price', Float),
             Column('fuel_type', String),
             Column('transmission', String),
             Column('features', JSON),
             Column('created_at', TIMESTAMP))

def create_table_if_not_exists():
    """
    Create the cars table if it does not exist.
    """
    if not engine.dialect.has_table(engine, 'cars'):
        metadata.create_all(engine)
        logging.info("Successfully created the cars table")
    else:
        logging.info("Cars table already exists")

def load_data(engine, data):
    """
    Load data into the cars table.

    :param engine: SQLAlchemy engine instance.
    :param data: Data to be inserted into the table.
    """
    create_table_if_not_exists()
    with engine.connect() as conn:
        try:
            conn.execute(cars.insert(), data)
            logging.info("Successfully inserted data into the cars table")
        except SQLAlchemyError as e:
            logging.error(f"Error inserting data: {e}")
