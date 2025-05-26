class Player:
    def __init__(self,firstName, lastName, age, nation):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__nation = nation
        
    def set_first_name(self,firstName):
        self.__firstName = firstName
        
    def get_first_name(self):
        return self.__firstName
    
    
    def set_last_name(self,lastName):
        self.__lastName = lastName
        
    def get_last_name(self):
        return self.__lastName
    
    def set_age(self,age):
        self.__age = age
        
    def get_age(self):
        return self.__age
    
    def set_nation(self,nation):
        self.__nation = nation
        
    def get_nation(self):
        return self.__nation
    
    def print_player(self):
        print("first name:",self.get_first_name())
        print("last name: ", self.get_last_name())
        print("age: ",self.get_age())
        print("nation: ",self.get_nation())

    
        