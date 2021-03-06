import db_create
from project import app, db
from flask.ext.testing import TestCase
from flask.ext.login import current_user
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

class  UsersViewsTests(BaseTestCase):
        # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)
        self.assertEqual(response.status_code, 200)

    # Ensure that the login behaves correctly given the correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.login_with_default_user()
            self.assertIn('You were logged in', response.data)
            self.assertTrue(current_user.is_active)

    # Ensure that the login behaves correctly given the incorrect credentials
    def test_incorrected_login(self):
        response = self.client.post(
            '/login',
            data=dict(username='a', password='admin'),
            follow_redirects=True)
        self.assertIn('Invalid Credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.login_with_default_user()
            response = self.client.get(
                '/logout',
                follow_redirects=True)
            self.assertIn('You were logged out.', response.data)
            self.assertFalse(current_user.is_active)

    def login_with_default_user(self):
        return self.client.post(
            '/login',
            data=dict(username='admin', password='Test@123'),
            follow_redirects=True)

    # Ensure user can register
    def test_user_registration(self):
        with self.client:
            response = self.client.post(
                '/register',
                data=dict(
                    username='John',
                    email='john@a.com',
                    password='Test@123',
                    confirm='Test@123'),
                follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == 'John')
            self.assertTrue(current_user.is_active())


if __name__ == '__main__':
    unittest.main()
