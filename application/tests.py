import unittest
from application import create_app, db


class TestInterviewer(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('development')
        self.client = self.app.test_client

        """Empty request for testing"""
        self.empty_request = {}

        """Define some interviewers for testing"""
        self.interviewer = {'name': 'Denis', 'department': 'IT'}

        """Define some interviewees for testing"""
        self.interviewee = {
            'name': 'John',
            'email': 'john@snow.com',
            'linked_in': 'https://www.linkedin.com/in/silvadenisaraujo/'
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_create_empty_interviewer(self):
        res = self.client().post('/interviewer/', data=self.empty_request)
        self.assertEqual(res.status_code, 400)

    def test_interviewer_creation(self):
        res = self.client().post('/interviewer/', data=self.interviewer)
        self.assertEqual(res.status_code, 200)

    def test_create_empty_interviewee(self):
        res = self.client().post('/interviewee/', data=self.empty_request)
        self.assertEqual(res.status_code, 400)

    def test_interviewee_creation(self):
        res = self.client().post('/interviewee/', data=self.interviewee)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
