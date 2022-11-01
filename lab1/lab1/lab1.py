from User import User
import sys

user = User("user1", "usr", 21, "url.danil21@gmail.com")
sizeInstance = sys.getsizeof(user)
print(f"size instance: {sizeInstance}")

user = User("user2", "usr", 21, "url.danil21@gmail.com")
user = User("user3", "usr", 21, "url.danil21@gmail.com")
user = User("user4", "usr", 21, "url.danil21@gmail.com")

print(f"count instances: {user.instancesCount}")
print(f"size all instances: {sizeInstance * user.instancesCount} byte")
