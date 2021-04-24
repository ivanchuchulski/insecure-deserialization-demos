import yaml
from user import User

user = User('spam', 'eggs')

with open('user.bin', 'w') as users:
    yaml.dump(user, users)

with open('user.bin', 'r') as users:
    deserialized_user = yaml.safe_load(users)

print("name: {}, surname: {}".format(deserialized_user.name, deserialized_user.surname))