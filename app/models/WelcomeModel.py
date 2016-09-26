""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def get_users(self, email):
        query = 'SELECT name FROM users WHERE email = :email'
        data = {'email': email}
        return self.db.query_db(query, data)

    def add_users(self, name, alias, email, password,date):
        password1 = self.bcrypt.generate_password_hash(password)
        print password1
        queryStr = "INSERT INTO users (name, alias, email, password, date, created_at, updated_at) VALUES (:name, :alias, :email, :password, :date, NOW(), NOW())"
        data = {'name': name.lower(), 'alias': alias,'email': email, 'password': password, 'date': date }
        return self.db.query_db(queryStr, data)
 
    def get_id(self,email):
        query = "SELECT id FROM users WHERE email = :email"
        data = {'email': email}
        return self.db.query_db(query,data)

    def get_name(self):
        query = "SELECT name FROM users"
        return self.db.query_db(query)

    def friends_info(self,name):
        query = "SELECT name, email FROM users WHERE name = :name"
        data = {'name': name}
        return self.db.query_db(query,data)

    def add_friends(self, name,users_id):
        query = "LEFT JOIN friendships on users.id = friendships.users_id INSERT INTO friendships (name,created_at, updated_at,users_id) VALUES (:name, NOW(), NOW(),:user_id)"
        data = {'name': name, 'users_id':1}
        return self.db.query_db(query,data)


    def login_user(self, email):
        #password = info['password']
        user_query = "SELECT password FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': email}
 # same as query_db() but returns one result
        #user = self.db.get_one(user_query, user_data)
        #if user_query == password:
        return self.db.query_db(user_query,user_data)
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """