class User:
# pass gets rid of the need to fill in the class or function.

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
#     it's convention that the name of the parameter is equal to the name of the attribute.

user_1 = User("001", "Bekir")
# instead of below, check what's above this line.
# user_1.id = "007"
# user_1.username = "Name"
print(user_1)

print(user_1.id)
# this prints the id