
class User:
    instancesCount = 0

    def __init__(self, firstname, lastName, age, email):
        User.instancesCount += 1
        self.__firstName = firstname
        self.lastName = lastName 
        self.__age = age
        self.email = email

    def set_age(self, age):
       if 1 < age < 110:
            self.__age = age
       else:
            print("Incorrect user age")
 
    def get_age(self):
        return self.__age
 
    def get_name(self):
        return self.__firstName

    def displayInfo(self):
        print(f"First name: {self.__firstName} \n Last name: {self.lastName} \n age:{self.__age} \n email: {self.email}")


    
    




