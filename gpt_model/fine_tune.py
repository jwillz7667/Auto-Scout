import openai
import json
import os
from datetime import datetime

# Load environment variables from .env file if present
from dotenv import load_dotenv
load_dotenv()

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def load_dataset(file_path):
    """
    Load the dataset for fine-tuning the GPT model.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def fine_tune_model(training_data, model_name="curie"):
    """
    Fine-tune the GPT model with the given training data.
    """
    response = openai.FineTune.create(
        training_file=training_data,
        model=model_name
    )
    return response

def save_fine_tuned_model(response, save_path):
    """
    Save the fine-tuned model details to a file.
    """
    with open(save_path, 'w') as file:
        json.dump(response, file, indent=4)
    print(f"Fine-tuned model details saved to {save_path}")

# Example usage
if __name__ == "__main__":
    dataset_path = 'path/to/your/dataset.json'  # Update with your dataset path
    save_path = f'models/fine_tuned_model_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    training_data = load_dataset(dataset_path)
    response = fine_tune_model(training_data)
    save_fine_tuned_model(response, save_path)
