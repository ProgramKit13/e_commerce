class User():
    def __init__(self, name, email, password, cpf, genre, token):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__cpf = cpf
        self.__genre = genre
        self.__token = token


    
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
    def cpf(self):
        return self.__cpf
        
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf= cpf

    @property
    def genre(self):
        return self.__genre
        
    @genre.setter
    def genre(self, genre):
        self.__genre= genre

    
    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token
