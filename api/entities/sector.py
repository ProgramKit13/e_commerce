class Sector():
    def __init__(self, id, name, token):
        self.id = id
        self.name = name
        self.token = token

    @property
    def name(self):
        return self.__name   
    @name.setter
    def name(self, name):
        self.__name= name


    @property
    def token(self):
        return self.__token    
    @token.setter
    def token(self, token):
        self.__token= token
