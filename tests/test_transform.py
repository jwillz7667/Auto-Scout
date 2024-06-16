import unittest
import logging
from data_pipeline.transform import transform_car_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestTransformCarData(unittest.TestCase):
    def test_transform_car_data(self):
        raw_data = {'model': 'Camry', 'price': '$24,000'}
        try:
            transformed_data = transform_car_data(raw_data)
            self.assertIsNotNone(transformed_data)
            self.assertEqual(transformed_data['model'], 'Camry')
            self.assertEqual(transformed_data['price'], 24000.0)
        except Exception as e:
            logging.error(f"An error occurred during test_transform_car_data: {e}")
            self.fail(f"test_transform_car_data failed due to an exception: {e}")

    def test_transform_car_data_missing_price(self):
        raw_data = {'model': 'Camry'}
        try:
            transformed_data = transform_car_data(raw_data)
            self.assertIsNone(transformed_data['price'])
        except Exception as e:
            logging.error(f"An error occurred during test_transform_car_data_missing_price: {e}")
            self.fail(f"test_transform_car_data_missing_price failed due to an exception: {e}")

if __name__ == '__main__':
    unittest.main()
