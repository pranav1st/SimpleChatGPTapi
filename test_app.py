import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the ChatGPT Flask app', response.data)

    def test_results_page(self):
        response = self.app.post('/results', data=dict(user_input="What is the meaning of life?"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'What is the meaning of life?', response.data)

    def test_api_error_handling(self):
        app.config['TESTING'] = True
        with app.test_client() as client:
            response = client.post('/results', data=dict(user_input="test"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Sorry, there was an error generating a response.", response.data)

if __name__ == '__main__':
    unittest.main()
