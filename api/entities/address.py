class Address():
    def __init__(self, neighborhood, street, number, state, city, zipCode, tokenUser, activate, complement):
        self.__neighborhood = neighborhood
        self.__street = street
        self.__number = number
        self.__state = state
        self.__city = city
        self.__zipCode = zipCode
        self.__tokenUser = tokenUser
        self.__activate = activate
        self.__complement = complement


    
    @property
    def street(self):
        return self.__street
        
    @street.setter
    def street(self, street):
        self.__street = street

    
    @property
    def neighborhood(self):
        return self.__neighborhood
        
    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

    
    @property
    def number(self):
        return self.__number
        
    @number.setter
    def number(self, number):
        self.__number= number

    
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
    def zipCode(self):
        return self.__zipCode
        
    @zipCode.setter
    def zipCode(self, zipCode):
        self.__zipCode= zipCode


    @property
    def activate(self):
        return self.__activate
        
    @activate.setter
    def activate(self, activate):
        self.__activate= activate

    
    @property
    def tokenUser(self):
        return self.__tokenUser
        
    @tokenUser.setter
    def tokenUser(self, tokenUser):
        self.__tokenUser= tokenUser

    
    @property
    def complement(self):
        return self.__complement
        
    @complement.setter
    def complement(self, complement):
        self.__complement = complement






        
