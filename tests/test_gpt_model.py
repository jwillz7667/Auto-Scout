import unittest
from gpt_model.fine_tune import fine_tune_model
from gpt_model.generate_responses import generate_response

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
        self.assertEqual(response['status'], 'succeeded')
        self.assertEqual(response['fine_tuned_model'], 'curie-finetuned')

class TestGenerateResponse(unittest.TestCase):
    def test_generate_response(self):
        prompt = "What are the best car options for a family of four?"
        response = generate_response(prompt)
        self.assertIsNotNone(response)
        self.assertTrue(len(response) > 0)

if __name__ == '__main__':
    unittest.main()
