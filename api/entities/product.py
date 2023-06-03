class Product():
    def __init__(self, prodName, valueResale, cust, tax, supplier, qt, discount, description, datePurchase, token):
        self.__prodName = prodName
        self.__valueResale = valueResale
        self.__cust = cust
        self.__tax = tax
        self.__supplier = supplier
        self.__qt = qt
        self.__discount = discount
        self.__description = description
        self.__datePurchase = datePurchase
        self.__token = token


    
    @property
    def prodName(self):
        return self.__prodName
        
    @prodName.setter
    def prodName(self, prodName):
        self.__prodName = prodName

        

    @property
    def valueResale(self):
        return self.__valueResale
        
    @valueResale.setter
    def valueResale(self, valueResale):
        self.__valueResale = valueResale

    
    @property
    def cust(self):
        return self.__cust
        
    @cust.setter
    def cust(self, cust):
        self.__cust= cust

    
    @property
    def tax(self):
        return self.__tax
        
    @tax.setter
    def tax(self, tax):
        self.__tax= tax

    @property
    def supplier(self):
        return self.__supplier
        
    @supplier.setter
    def supplier(self, supplier):
        self.__supplier= supplier

    @property
    def qt(self):
        return self.__qt
        
    @qt.setter
    def qt(self, qt):
        self.__qt= qt

    @property
    def discount(self):
        return self.__discount
        
    @discount.setter
    def discount(self, discount):
        self.__discount= discount


    @property
    def description(self):
        return self.__description
        
    @description.setter
    def description(self, description):
        self.__description = description
    

    @property
    def datePurchase(self):
        return self.__datePurchase
        
    @datePurchase.setter
    def datePurchase(self, datePurchase):
        self.__datePurchase = datePurchase


    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token= token

