import db_create
from project import app, db
from flask.ext.testing import TestCase
import unittest


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db_create.create()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)
        self.assertEqual(response.status_code, 200)

    # Ensure that the login behaves correctly given the correct credentials
    def test_correct_login(self):
        response = self.client.post(
            '/login',
            data=dict(username='admin', password='Teste@123'),
            follow_redirects=True)
        self.assertIn('You were logged in', response.data)

    # Ensure that the login behaves correctly given the incorrect credentials
    def test_incorrected_login(self):
        response = self.client.post(
            '/login',
            data=dict(username='a', password='admin'),
            follow_redirects=True)
        self.assertIn('Invalid Credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        self.client.post(
            '/login',
            data=dict(username='admin', password='Teste@123'),
            follow_redirects=True)
        response = self.client.get(
            '/logout',
            follow_redirects=True)
        self.assertIn('You were logged out.', response.data)

if __name__ == '__main__':
    unittest.main()
