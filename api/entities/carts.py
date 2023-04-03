class Carts():
    def __init__(self, qt, value, confirm, totalDiscount, tokenProduct, tokenUser, tokenPayment, token):
        self.__qt = qt
        self.__value = value
        self.__confirm = confirm
        self.__totalDiscount = totalDiscount
        self.__tokenUser = tokenUser
        self.__qt = qt
        self.__tokenPayment = tokenPayment
        self.__token = token
        self.__tokenProduct = tokenProduct


    
    @property
    def qt(self):
        return self.__qt
        
    @qt.setter
    def qt(self, qt):
        self.__qt = qt

        
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        self.__value = value

    
    @property
    def confirm(self):
        return self.__confirm
        
    @confirm.setter
    def confirm(self, confirm):
        self.__confirm= confirm

    
    @property
    def totalDiscount(self):
        return self.__totalDiscount
        
    @totalDiscount.setter
    def totalDiscount(self, totalDiscount):
        self.__totalDiscount= totalDiscount

    @property
    def tokenUser(self):
        return self.__tokenUser
        
    @tokenUser.setter
    def tokenUser(self, tokenUser):
        self.__tokenUser= tokenUser

    @property
    def tokenPayment(self):
        return self.__tokenPayment
        
    @tokenPayment.setter
    def tokenPayment(self, tokenPayment):
        self.__tokenPayment= tokenPayment
    
    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token


    
    @property
    def tokenProduct(self):
        return self.__tokenProduct
        
    @tokenProduct.setter
    def tokenProduct(self, tokenProduct):
        self.__tokenProduct= tokenProduct
