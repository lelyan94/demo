import unittest
from server import app, host, port

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        # Create a test client using the Flask application configured for testing
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_1_server_running(self):
        expected_host = "0.0.0.0"
        expected_port = 3000
        self.assertEqual(host, expected_host)
        self.assertEqual(port, expected_port)
        print(f"\n✔ Testing web server running on http://{host}:{port}")

    def test_2_index(self):
        # Send a GET request to the '/' URL and capture the response
        response = self.app.get('/')
        # Assert that the HTTP status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        print("\n✔ responds to /")
        # Assert that the response data matches what is expected
        # self.assertIn('CPSY 350 Project: Jenkins CI/CD Pipeline. SAIT ID:000123456\n', response.data.decode())

    def test_3_404(self):
        # Test for non-existent paths
        response = self.app.get('/nonexistentpath')
        # Assert that the HTTP status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)
        print("\n✔ 404 everything else")

if __name__ == '__main__':
    unittest.main()

