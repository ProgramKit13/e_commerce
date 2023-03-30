class Carts():
    def __init__(self, qt, value, confirm, totalDiscount, idProduct, idPayment, token):
        self.__qt = qt
        self.__value = value
        self.__confirm = confirm
        self.__totalDiscount = totalDiscount
        self.__idProduct = idProduct
        self.__qt = qt
        self.__idPayment = idPayment
        self.__token = token


    
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
    def idProduct(self):
        return self.__idProduct
        
    @idProduct.setter
    def idProduct(self, idProduct):
        self.__idProduct= idProduct

    @property
    def idPayment(self):
        return self.__idPayment
        
    @idPayment.setter
    def idPayment(self, idPayment):
        self.__idPayment= idPayment
    
    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token


        
