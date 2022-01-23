from flask_login import UserMixin
from  uuid import uuid4

class User(UserMixin): 
    id='' 
    login=''
    passwd='' 

    def __init__(self,login,passwd):
        print ('class User initialized')
        self.id=str(uuid4())
        self.login=login
        self.passwd=passwd

users_passwd={ 
   'user':'password',
   'testuser':'testpass'
}

class Users(): 
    sessions={} 
    logins={} 
    
    def __init__(self,users): 
        for login in users.keys(): 
            user=User(login, users[login]) 
            self.logins[login]=user 

UserBase=Users(users_passwd) 



