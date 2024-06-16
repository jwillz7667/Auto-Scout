import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_connection import metadata
from data_pipeline.load import load_data
from database.models import cars

class TestLoadData(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.engine = create_engine('sqlite:///:memory:')
        metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def test_load_data(self):
        sample_data = {
            'make': 'Toyota', 'model': 'Camry', 'year': 2021, 'price': 24000,
            'fuel_type': 'Gasoline', 'transmission': 'Automatic', 'features': {}, 'created_at': '2023-01-01T00:00:00'
        }
        load_data(self.engine, sample_data)
        result = self.session.query(cars).filter_by(model='Camry').one()
        self.assertEqual(result.model, 'Camry')
        self.assertEqual(result.price, 24000.0)

if __name__ == '__main__':
    unittest.main()
