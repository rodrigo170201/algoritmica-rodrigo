class Client:
    
    #GENRE = ['M','F']
    #Constructor
    def __init__(self, name, lastname, phone, email, address):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address
    
    def __init__ (self):
        pass

    #Getters
    def get_name(self):
        return self.name
    
    def get_lastName(self):
        return self.lastname
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_address(self):
        return self.address
    
    