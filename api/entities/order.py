class Order():
    def __init__(self, tokenProduct, tokenUser, tokenCart, token, qt, value, discount):
        self.tokenProduct = tokenProduct
        self.tokenUser = tokenUser
        self.tokenCart = tokenCart
        self.token = token
        self.qt = qt
        self.value = value
        self.discount = discount
    
    @property
    def tokenProduct(self):
        return self.__tokenProduct
        
    @tokenProduct.setter
    def tokenProduct(self, tokenProduct):
        self.__tokenProduct = tokenProduct

    @property
    def tokenUser(self):
        return self.__tokenUser
    def tokenUser(self, tokenUser):
        self.__tokenUser = tokenUser

    @property
    def tokenCart(self):
        return self.__tokenCart
    def tokenCart(self, tokenCart):
        self.__tokenCart = tokenCart

    @property
    def token(self):
        return self.__token
    def token(self, token):
        self.__token = token
    
    @property
    def qt(self):
        return self.__qt
    def qt(self, qt):
        self.__qt = qt

    @property
    def value(self):
        return self.__value
    def value(self, value):
        self.__value = value

    @property
    def discount(self):
        return self.__discount
    def discount(self, discount):
        self.__discount = discount