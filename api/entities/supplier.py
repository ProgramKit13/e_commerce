class Supplier():
    def __init__(self, name, email, uf, city, neighborhood, number, complement, cnpj, idProduct):
        self.__name = name
        self.__email = email
        self.__uf = uf
        self.__city = city
        self.__neighborhood = neighborhood
        self.__number = number
        self.__complement = complement
        self.__cpj = cnpj
        self.__idProduct = idProduct


    
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
    def uf(self):
        return self.__uf
        
    @uf.setter
    def uf(self, uf):
        self.__uf= uf


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
    def idProduct(self):
        return self.__idProduct
        
    @idProduct.setter
    def idProduct(self, idProduct):
        self.__idProduct= idProduct

        
