from flask.wrappers import Response
from tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user
from flask.wrappers import Response

class TestLogin(BaseTest):
    # test signing up user successfully
    def login(self, email, passwordEntered):
        with self.app:
            response = self.app.get('/log-in', data=dict(
            email=email,
            password=passwordEntered
        ), follow_redirects=True)

def test_login_logout(self):
    "Make sure login and logout works."
    rv = (self, db.session.query(User).data.config['email'], db.session.query(User).config['PASSWORD'])
    assert b'You were logged in' in rv.data

    rv = (self)
    assert b'You were logged out' in rv.data

    rv = (self, db.session.query(User).config['email'] + 'x', db.session.query(User).config['PASSWORD'])
    assert b'Invalid username' in rv.data

    rv = (self, db.session.query(User).config['email'], db.session.query(User).config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data
