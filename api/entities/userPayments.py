class Supplier():
    def __init__(self, typePayment, value, status, userToken, datePayment, dateStatus):
        self.__typePayment = typePayment
        self.__value = value
        self.__status = status
        self.__userToken = userToken
        self.__datePayment = datePayment
        self.__dateStatus = dateStatus

    
    @property
    def typePayment(self):
        return self.__typePayment
        
    @typePayment.setter
    def typePayment(self, typePayment):
        self.__typePayment = typePayment

        
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        self.__value = value

    
    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, status):
        self.__status= status


    @property
    def userToken(self):
        return self.__userToken
        
    @userToken.setter
    def userToken(self, userToken):
        self.userToken= userToken

    @property
    def datePayment(self):
        return self.__datePayment
        
    @datePayment.setter
    def datePayment(self, datePayment):
        self.__datePayment= datePayment

    @property
    def dateStatus(self):
        return self.__dateStatus
        
    @dateStatus.setter
    def dateStatus(self, dateStatus):
        self.__dateStatus= dateStatus

        
