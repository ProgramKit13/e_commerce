class Supplier():
    def __init__(self, supplierName, supplierEmail, supplierState, supplierCity, supplierNeighborhood, supplierStreet, supplierNumber, supplierComplement, supplierZipCode, supplierCnpj, token, supplierPhone_01, supplierPhone_02):
        self.supplierName = supplierName
        self.supplierEmail = supplierEmail
        self.supplierState = supplierState
        self.supplierCity = supplierCity
        self.supplierNeighborhood = supplierNeighborhood
        self.supplierStreet = supplierStreet
        self.supplierNumber = supplierNumber
        self.supplierComplement = supplierComplement
        self.supplierZipCode = supplierZipCode
        self.supplierCnpj = supplierCnpj
        self.supplierPhone_01 = supplierPhone_01
        self.supplierPhone_02 = supplierPhone_02
        self.token = token

    @property
    def supplierName(self):
        return self.__supplierName
    
    @supplierName.setter
    def supplierName(self, supplierName):
        self.__supplierName = supplierName


    @property
    def supplierEmail(self):
        return self.__supplierEmail
    
    @supplierEmail.setter
    def supplierEmail(self, supplierEmail):
        self.__supplierEmail = supplierEmail


    @property
    def supplierState(self):
        return self.__supplierState
    
    @supplierState.setter
    def supplierState(self, supplierState):
        self.__supplierState = supplierState


    @property
    def supplierCity(self):
        return self.__supplierCity
    
    @supplierCity.setter
    def supplierCity(self, supplierCity):
        self.__supplierCity = supplierCity

    
    @property
    def supplierNeighborhood(self):
        return self.__supplierNeighborhood
    
    @supplierNeighborhood.setter
    def supplierNeighborhood(self, supplierNeighborhood):
        self.__supplierNeighborhood = supplierNeighborhood


    @property
    def supplierStreet(self):
        return self.__supplierStreet
    
    @supplierStreet.setter
    def supplierStreet(self, supplierStreet):
        self.__supplierStreet = supplierStreet


    @property
    def supplierNumber(self):
        return self.__supplierNumber
    
    @supplierNumber.setter
    def supplierNumber(self, supplierNumber):
        self.__supplierNumber = supplierNumber


    @property
    def supplierComplement(self):
        return self.__supplierComplement
    
    @supplierComplement.setter
    def supplierComplement(self, supplierComplement):
        self.__supplierComplement = supplierComplement


    @property
    def supplierZipCode(self):
        return self.__supplierZipCode
    
    @supplierZipCode.setter
    def supplierZipCode(self, supplierZipCode):
        self.__supplierZipCode = supplierZipCode


    @property
    def supplierCnpj(self):
        return self.__supplierCnpj
    
    @supplierCnpj.setter
    def supplierCnpj(self, supplierCnpj):
        self.__supplierCnpj = supplierCnpj


    @property
    def supplierPhone_01(self):
        return self.__supplierPhone_01

    @supplierPhone_01.setter
    def supplierPhone_01(self, supplierPhone_01):
        self.__supplierPhone_01 = supplierPhone_01


    @property
    def supplierPhone_02(self):
        return self.__supplierPhone_02
    
    @supplierPhone_02.setter
    def supplierPhone_02(self, supplierPhone_02):
        self.__supplierPhone_02 = supplierPhone_02


    @property
    def token(self):
        return self.__token
    
    @token.setter
    def token(self, token):
        self.__token = token