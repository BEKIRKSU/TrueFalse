class User:
# pass gets rid of the need to fill in the class or function.
# Instead we have an __init__ which is an initialiser with parameters. Such as id and username.
     def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
#     it's convention that the name of the parameter is equal to the name of the attribute.

user_1 = User("001", "Bekir")
# instead of below, check what's above this line.
# user_1.id = "007"
# user_1.username = "Name"
print(user_1.username)
# When printing be specific.

user_1 = User("007", "Bekir")
# much easier to make an object with 2 arguments. More convenient.


# this prints the id