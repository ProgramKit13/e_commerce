class User():
    def __init__(self, firstName, lastName, email, password, cpf, genre, dateCreation, token):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__password = password
        self.__cpf = cpf
        self.__genre = genre
        self.__dateCreation = dateCreation
        self.__token = token


    
    @property
    def firstName(self):
        return self.__firstName
        
    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
        
    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

        
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
