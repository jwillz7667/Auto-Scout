import openai
import json
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
import json
import os

def load_dataset(file_path):
    """
    Load the dataset for fine-tuning the GPT model.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        raise
    return data

def fine_tune_model(training_data, model_name="curie"):
    """
    Fine-tune the GPT model with the given training data.
    """
    try:
        response = openai.FineTune.create(
            training_file=training_data,
            model=model_name
        )
    except openai.error.OpenAIError as e:
        logging.error(f"Error during fine-tuning: {e}")
        raise
    return response

def save_fine_tuned_model(response, save_path):
    """
    Save the fine-tuned model details to a file.
    """
    try:
        with open(save_path, 'w') as file:
            json.dump(response, file, indent=4)
        logging.info(f"Fine-tuned model details saved to {save_path}")
    except IOError as e:
        logging.error(f"Error saving fine-tuned model details: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        dataset_path = 'path/to/your/dataset.json'  # Update with your dataset path
        save_path = f'models/fine_tuned_model_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        training_data = load_dataset(dataset_path)
        response = fine_tune_model(training_data)
        save_fine_tuned_model(response, save_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
