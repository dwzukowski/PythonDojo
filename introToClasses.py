

#declare class User
class User(object):
    #init method called every time a new object is created; 
    def __init__(self,name,email):
        #set some instance variables. can be named anything
        self.name = name
        self.email = email
        self.logged = False
        #method to help user login
        def login(self):
            self.logged = True
            print self.name + "is logged in."
            return self
#now create an instance of the class

new_user = User("Anna","anna@anna.com")
print new_user
print new_user.name
print new_user.logged
print new_user.email
print "*******"
user1 = User("Anna", "anna@anna.com")
print user1
print user1.name
print user1.logged
print user1.email

"""
michael = User()
anna = User()
print michael
print anna
"""