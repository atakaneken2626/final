class Player:
    def __init__(self, firstName, lastName, age, nation):
        self.fn = firstName
        self.ln = lastName
        self.a = age
        self.n = nation
        
    def set_firstName(self, x):
        self.fn = x
        
    def set_lastName(self, x):
        self.ln = x
        
    def set_age(self, x):
        self.a = x
        
    def set_nation(self, x):
        self.n = x
        
    def get_firstName(self):
        return self.fn
    
    def get_lastName(self):
        return self.ln
    
    def get_age(self):
        return self.a
    
    def get_nation(self):
        return self.n
    
    def print_player(self):
            print("first name: ", self.get_firstName())
            print("last name: ", self.get_lastName())
            print("age: ", self.get_age())
            print("nation: ", self.get_nation())
    
    
        
    
        