from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_car_data(car_data):
    """
    Transform car data by converting price to float and adding a timestamp.

    :param car_data: Dictionary containing car data.
    :return: Transformed car data or None if an error occurs.
    """
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
