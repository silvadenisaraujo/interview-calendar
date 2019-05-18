import unittest
import app


class TestSlot(unittest.TestCase):

    def setUp(self):
        app = app.test_client()
        self.response = app.get('/slots')

    def test_get(self):
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
