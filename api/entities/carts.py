class Cart:
    def __init__(self, id, tokenUser, token, discountTotal, valueTtotal, openCart, status):
        self.id = id
        self.tokenUser = tokenUser
        self.token = token
        self.discountTotal = discountTotal
        self.valueTtotal = valueTtotal
        self.openCart = openCart
        self.status = status
    
    @property
    def tokenUser(self):
        return self.__tokenUser
        
    @tokenUser.setter
    def prodName(self, tokenUser):
        self.__tokenUser = tokenUser
    
    @property
    def token(self):
        return self.__token
    @token.setter
    def token(self, token):
        self.__token = token
    
    @property
    def discountTotal(self):
        return self.__discountTotal
    @discountTotal.setter
    def discountTotal(self, discountTotal):
        self.__discountTotal = discountTotal

    @property
    def valueTtotal(self):
        return self.__valueTtotal
    @valueTtotal.setter
    def valueTtotal(self, valueTtotal):
        self.__valueTtotal = valueTtotal

    @property
    def openCart(self):
        return self.__openCart
    @openCart.setter
    def openCart(self, openCart):
        self.__openCart = openCart

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status
