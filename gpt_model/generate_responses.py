import openai
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

def generate_response(prompt, model="curie"):
    """
    Generate a response using the fine-tuned GPT model.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        logging.error(f"Error generating response: {e}")
        raise
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "What are the best car options for a family of four?"
    try:
        response = generate_response(prompt)
        print(response)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
