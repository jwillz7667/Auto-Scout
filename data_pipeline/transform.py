from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_car_data(car_data):
    try:
        if 'price' in car_data:
            car_data['price'] = float(car_data['price'].replace('$', '').replace(',', ''))
        else:
            logging.warning("Price key not found in data")
            car_data['price'] = None

        car_data['created_at'] = datetime.now().isoformat()
        logging.info("Successfully transformed car data")
        return car_data
    except (ValueError, KeyError) as e:
        logging.error(f"Error transforming data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    raw_data = {'model': 'Camry', 'price': '$24,000'}
    transformed_data = transform_car_data(raw_data)
    print(transformed_data)
