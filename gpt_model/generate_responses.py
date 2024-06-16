import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(prompt, model="curie"):
    """
    Generate a response using the fine-tuned GPT model.
    """
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    prompt = "What are the best car options for a family of four?"
    response = generate_response(prompt)
    print(response)
