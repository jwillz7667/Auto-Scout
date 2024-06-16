import unittest
from data_pipeline.transform import transform_car_data

class TestTransformCarData(unittest.TestCase):
    def test_transform_car_data(self):
        raw_data = {'model': 'Camry', 'price': '$24,000'}
        transformed_data = transform_car_data(raw_data)
        self.assertIsNotNone(transformed_data)
        self.assertEqual(transformed_data['model'], 'Camry')
        self.assertEqual(transformed_data['price'], 24000.0)

    def test_transform_car_data_missing_price(self):
        raw_data = {'model': 'Camry'}
        transformed_data = transform_car_data(raw_data)
        self.assertIsNone(transformed_data['price'])

if __name__ == '__main__':
    unittest.main()
