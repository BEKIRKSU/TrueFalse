class User:
# pass gets rid of the need to fill in the class or function.
# Instead we have an __init__ which is an initialiser with parameters. Such as id and username.
# You can add an attribute without making it an argumnt, so it's not inside the parantheses but it's
# still set. So all objects being created from this calss will have a 'follower' attribute that's set
# out to 0 to begin with. So it doesn't need to be in the initializer (parantheses)
     def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
#     it's convention that the name of the parameter is equal to the name of the attribute.
     def follow(self, user):
         user.followers += 1
         self.following += 1
# You use self when writing inside a class.


user_1 = User("001", "Bekir")
# instead of below, check what's above this line.
# user_1.id = "007"
# user_1.username = "Name"
print(user_1.username)
# When printing be specific.

user_2 = User("007", "Bekir")
# much easier to make an object with 2 arguments. More convenient.
print(user_1.followers)
# This will print '0' although it's not an argument in the initializer. Because the class has a set
# attribute.

#  attributes and methods. Methods are used to possibly change the attributes.
# So we'll have a function inside a class (it's called a method when this is the case)
# Methods look the same as functions, def name(): body.
# it then get's the object, so 'self' and changes the attribute 'seats' like
# def name():
#    self.seats = 2

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)