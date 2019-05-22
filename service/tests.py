import unittest
from service import app


class TestInterviewer(unittest.TestCase):

    def setUp(self):
        self.application = app.test_client()

    def test_create_interviewer(self):
        data = {
            'name': 'Denis'
        }
        response = self.application.post('/interviewer', data)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
