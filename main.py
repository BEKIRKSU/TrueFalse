class User:
# pass gets rid of the need to fill in the class or function.
# Instead we have an __init__ which is an initialiser with parameters. Such as id and username.
# You can add an attribute without making it an argumnt, so it's not inside the parantheses but it's
# still set. So all objects being created from this calss will have a 'follower' attribute that's set
# out to 0 to begin with. So it doesn't need to be in the initializer (parantheses)
     def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
#     it's convention that the name of the parameter is equal to the name of the attribute.

user_1 = User("001", "Bekir")
# instead of below, check what's above this line.
# user_1.id = "007"
# user_1.username = "Name"
print(user_1.username)
# When printing be specific.

user_2 = User("007", "Bekir")
# much easier to make an object with 2 arguments. More convenient.
print(user_1.follower)
# This will print '0' although it's not an argument in the initializer. Because the class has a set
# attribute.


# this prints the id