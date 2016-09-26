"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
import re
from flask import escape
from flask import flash
from system.core.controller import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        #if 'user_id' in session and 'name' in session:
        #    return self.load_view('success.html',id=id)
        return self.load_view('index.html')

    def login(self):  
        post = request.form 
        if 'email' in post and 'password' in post: 
            #def edit(id):
            email = escape(post['email']).lower()
            password = escape(post['password'])
            #print email 
            #print password
            if email and password: 
                user= self.models['WelcomeModel'].get_users(email)
                user_id = self.models['WelcomeModel'].get_id(email)
               # print user_id
                session['name'] = user[0]['name']
                if user:

                # test password
                    user_query = self.models['WelcomeModel'].login_user(email)
                    #print user_query
                    #print password
                    if user_query[0]['password'] == password:
                        user_id = self.models['WelcomeModel'].get_id(email)
                        #set session and go to login
                        #print session['user_id']
                        id = user_id[0]['id']
                        #session['id'] = user[0]['id']
                        users = self.models['WelcomeModel'].get_name()
                        print users
                        return self.load_view('success.html',name = session['name'], users = users, id = id)    
                    else: 
                        flash("Email and password do not match", 'lg_email')

                    #else:
                    #    flash("Password cannot be blank", "password")
                flash("User does not exist in database. Register below!", 'lg_email')
            else:
                if not post['email']: flash("Email cannot be blank",'lg_email')
                if not post['password']: flash("Password cannot be blank",'lg_password')
            return redirect('/')

    def friends_show(self,name):
        session['name']=name
        #print session['id']
        users=self.models['WelcomeModel'].friends_info(name)
        return self.load_view('friendsInfo.html',name =session['name'], users = users)

    def add_friends(self,name):
        session['name']=name
        print session['name']
        users_id = id
        users = self.models['WelcomeModel'].friends_info(name)
        self.models['WelcomeModel'].add_friends(name,users_id)
        return self.load_view('success.html', users= users)

    def create(self):
    # because it's shorter
        post = request.form

    # test for post data
        if 'name' in post and 'email' in post and 'password' in post and 'passwordConfirm' in post and 'alias' in post and 'date' in post:

        # escape inputs
            name = escape(post['name'])
            alias = escape(post['alias'])
            email = escape(post['email'])
            password = escape(post['password'])
            passwordConfirm = escape(post['passwordConfirm'])
            date = escape(post['date'])

            err = False

        # validate inputs
            if not name:
                err = True
                flash("Name cannot be blank", "name")
            if not email:
                err = True
                flash("Email cannot be blank", "email")
            elif not EMAIL_REGEX.match(email):
                err = True
                flash("Invalid email address", "email")
            if not password:
                err = True
                flash("Password cannot be blank", "password")
            if not passwordConfirm:
                err = True
                flash("Password Confirmation cannot be blank", "passwordConfirm")
            if password and passwordConfirm and password != passwordConfirm:
                err = True          
                flash("Passwords do not match", "password")

        # if there were no errors
            if not err:

            # encrypt password
                err = True
                #encrypted_password = bcrypt.generate_password_hash(password)

            # insert user
                self.models['WelcomeModel'].add_users(name,alias,email,password,date)

            # set session
                #session['user_id'] = int(user_id)
                session['name'] = name
                users = self.models['WelcomeModel'].get_name()
                #user_id = self.models['WelcomeModel'].get_id(email)
                #id = user_id[0]['id']
                return self.load_view('success.html',users = users, name = name)

    # if it failed reload the login page
        return redirect('/')

    def logout(self):
        session.pop ('user_id', None)
        session.pop ('name', None)
        return self.load_view('index.html')
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """

