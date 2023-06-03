class User():
    def __init__(self, name, email, password, dateCreation, token, adminAccess):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__dateCreation = dateCreation
        self.__token = token
        self.__adminAccess = adminAccess
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name


        
    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, email):
        self.__email = email

        
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self, password):
        self.__password = password


    @property
    def dateCreation(self):
        return self.__dateCreation
        
    @dateCreation.setter
    def dateCreation(self, dateCreation):
        self.__dateCreation= dateCreation

    
    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token


    @property
    def adminAccess(self):
        return self.__adminAccess
        
    @adminAccess.setter
    def adminAccess(self, adminAccess):
        self.__adminAccess= adminAccess


    
