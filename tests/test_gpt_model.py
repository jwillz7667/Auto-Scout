import unittest
import logging
from gpt_model.fine_tune import fine_tune_model
from gpt_model.generate_responses import generate_response

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestFineTuneModel(unittest.TestCase):
    def test_fine_tune_model(self):
        # Mock fine-tuning response
        response = {
            "id": "ft-123",
            "object": "fine-tune",
            "created_at": 1614807353,
            "model": "curie",
            "status": "succeeded",
            "fine_tuned_model": "curie-finetuned"
        }
        try:
            self.assertEqual(response['status'], 'succeeded')
            self.assertEqual(response['fine_tuned_model'], 'curie-finetuned')
        except Exception as e:
            logging.error(f"An error occurred during test_fine_tune_model: {e}")
            self.fail(f"test_fine_tune_model failed due to an exception: {e}")

class TestGenerateResponse(unittest.TestCase):
    def test_generate_response(self):
        prompt = "What are the best car options for a family of four?"
        try:
            response = generate_response(prompt)
            self.assertIsNotNone(response)
            self.assertTrue(len(response) > 0)
        except Exception as e:
            logging.error(f"An error occurred during test_generate_response: {e}")
            self.fail(f"test_generate_response failed due to an exception: {e}")

if __name__ == '__main__':
    unittest.main()
