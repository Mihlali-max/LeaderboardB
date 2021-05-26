from flask.wrappers import Response
from tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user, AnonymousUserMixin
from flask.wrappers import Response
from flask import request

class TestLogin(BaseTest):

    def test_sign_up_post_success(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

            # Test valid user and valid password

            resp = self.app.post('/log-in', data =dict(email='email@gmail.com', password='pass1234'),follow_redirects=True)

            self.assertIn(b'Logged in successfully',resp.data)

    def test_login_Invalid_user(self):

        with self.app:
    # create a post req with valid data
            response = self.app.post('/sign-up',data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                                           password2='pass1234'),
                                                                 follow_redirects=True)
    # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

            #Test non-existing email


            respi = self.app.post('/log-in', data=dict(email='Mihlali@gmail.com'),
                                 follow_redirects=True)

            self.assertIn(b'Email does not exist', respi.data)

    def test_login_in_wrong_password(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

            #Test non- existing your password
            respa = self.app.post('/log-in', data=dict(email='email@gmail.com', password='passw482368or'),
                                 follow_redirects=True)
            self.assertIn(b'Password is wrong', respa.data)

    def logout_root_accessed(self):
        with self.app:
            response = self.app.post('/log-out', data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

            #test that route is accessed if user is logged in ( integration )
            def test_login_in_wrong_password(self):
                with self.app:
                    # create a post req with valid data
                    response = self.app.post('/sign-up',
                                             data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                                       password2='pass1234'),
                                             follow_redirects=True)
                    # assert that new user is created in db
                    user = db.session.query(User).filter_by(email='email@gmail.com').first()
                    self.assertTrue(user)
                    # assert that flash message is shown
                    self.assertIn(b'Account created', response.data)
                    # assert that user is logged in
                    self.assertEqual(current_user.get_id(), '1')
                    # assert that page is redirected
                    self.assertIn(b'Notes', response.data)

                    respa = self.app.get('/log-out', follow_redirects=True)

                    self.assertEqual(respa.status_code, 200)


            #test that route cant be accessed if user is not logged in (unit)

            self.assertEqual('http://localhost/log-in', request.url)

            #test response code when user navigates to page ( logged in ) (integration)

            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

            #test response code when user navigates to page ( not logged in ) (unit)

            rec = self.app.get('/log-out', follow_redirects=False)

            self.assertEqual(rec.status_code, 302)




