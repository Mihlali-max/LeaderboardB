from tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User


# test sign up
class TestSignUp(BaseTest):

    # test everyone can access /sign-up route
    def test_get_sign_up(self):
        # app test client
        with self.app:
            # assert that no user is signed in
            # cant test current user before get request ?
            # self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self)) # what even
            # go to route
            response = self.app.get('/sign-up', follow_redirects=True)
            # assert that the route name is correct
            self.assertIn('/sign-up', request.url)
            # assert that sign up page is rendered with correct content
            self.assertIn(b'<title>\nSign Up\n</title>', response.data)
            # assert status code 200
            self.assertEqual(response.status_code, 200)
            # assert that no user is signed in
            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))
            

    # test /sign up post req with an email less than 4 char
    def test_sign_up_post_short_email(self):
        with self.app:
            # create sign up post
            response = self.app.post('/sign-up',
                           data=dict(email='meh', firstName='NormalName', password1='pass1234', password2='pass1234'),
                           follow_redirects=True)
            # assert that flash message is returned
            self.assertIn(b'Email must be greater than 3 characters', response.data)
            # assert status code
            self.assertEqual(response.status_code, 200) # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='meh').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())


    # test sign up post if name is 1 char
    def test_sign_up_post_short_name(self):
        with self.app:
            # create post
            response = self.app.post('/sign-up', 
                                     data=dict(email='email@gmail.com', firstName='h', password1='pass1234', password2='pass1234'),
                                     follow_redirects=True)
            # assert that flash message appears
            self.assertIn(b'First name must be greater than 1 character', response.data)  
            # assert status code
            self.assertEqual(response.status_code, 200) # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id()) 


    # test sign up post if passwords don't match
    def test_sign_up_post_passwords_mismatched(self):
        with self.app:
            # create our post req
            response = self.app.post('/sign-up', 
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass6789'),
                                    follow_redirects=True)
            # assert flash message appears
            self.assertIn(b'Passwords don&#39;t match', response.data)  
            # assert status code
            self.assertEqual(response.status_code, 200) # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())

    def test_sign_up_password_atleast_7_Characters(self):
        with self.app:
            # create sign up post
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='NormalName', password1='pass12',
                                               password2='pass12'),
                                     follow_redirects=True)
            # assert that flash message is returned
            self.assertIn(b'Password must be at least 7 characters', response.data)
            # assert status code
            self.assertEqual(response.status_code, 200)  # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(password='pass12').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())


    def route_cant_be_accessed_if_user_is_not_logged_in(self):
        with self.app:
            # create sign up post
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='NormalName', password1='pass12',
                                               password2='pass12'),
                                     follow_redirects=True)
            # assert that flash message is returned
            self.assertIn(b'Password must be at least 7 characters', response.data)
            # assert status code
            self.assertEqual(response.status_code, 200)  # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(password='pass12').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())



