class Supplier():
    def __init__(self, typePayment, value, status, idUser, datePayment, dateStatus):
        self.__typePayment = typePayment
        self.__value = value
        self.__status = status
        self.__idUser = idUser
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
    def idUser(self):
        return self.__idUser
        
    @idUser.setter
    def idUser(self, idUser):
        self.__idUser= idUser

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

        
