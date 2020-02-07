import unittest

import os
 
from datingapp import app, db, mail
from datingapp.models import User
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
        # Disable sending emails during unit testing
        mail.init_app(app)
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    '''def test_valid_register(self):
        user = User('test123', 'Test@gmail.com', '123456', 'Female', 'Male')
        db.session.add(user)
        db.session.commit()
        #flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thanks for registering!', response.data)'''

    '''def test_invalid_register(self):
        response = register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsNotAwesome')
        self.assertIn(b'Field must be equal to password.', response.data)'''
    '''def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)'''

    '''def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)''' 
 
if __name__ == "__main__":
    unittest.main()