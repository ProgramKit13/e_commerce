class Supplier():
    def __init__(self, name, email, state, city, neighborhood, street, number, complement, zipCode, cnpj, token, phone):
        self.__name = name
        self.__email = email
        self.__state = state
        self.__city = city
        self.__neighborhood = neighborhood
        self.__street = street
        self.__number = number
        self.__complement = complement
        self.__zipCode = zipCode
        self.__cnpj = cnpj
        self.__token = token
        self.__phone = phone


    
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
    def state(self):
        return self.__state
        
    @state.setter
    def state(self, state):
        self.__state= state


    @property
    def city(self):
        return self.__city
        
    @city.setter
    def city(self, city):
        self.__city= city

    @property
    def neighborhood(self):
        return self.__neighborhood
        
    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood= neighborhood

    @property
    def number(self):
        return self.__number
        
    @number.setter
    def number(self, number):
        self.__number= number
    
    @property
    def complement(self):
        return self.__complement
        
    @complement.setter
    def complement(self, complement):
        self.__complement= complement


    @property
    def cnpj(self):
        return self.__cnpj
        
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj= cnpj

    
    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token

    
    @property
    def phone(self):
        return self.__phone
        
    @phone.setter
    def phone(self, phone):
        self.__phone= phone

    
    @property
    def street(self):
        return self.__street
        
    @street.setter
    def street(self, street):
        self.__street = street

    
    @property
    def zipCode(self):
        return self.__zipCode
        
    @zipCode.setter
    def zipCode(self, zipCode):
        self.__zipCode = zipCode


        

