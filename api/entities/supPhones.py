class SupPhones():
    def __init__(self, type, ddd, number, idSups):
        self.__type = type
        self.__ddd = ddd
        self.__cust = number
        self.__idSups = idSups


    
    @property
    def type(self):
        return self.__type
        
    @type.setter
    def type(self, type):
        self.__type = type

        
    @property
    def ddd(self):
        return self.__ddd
        
    @ddd.setter
    def ddd(self, ddd):
        self.__ddd = ddd

    
    @property
    def number(self):
        return self.__cust
        
    @number.setter
    def number(self, number):
        self.__cust= number

    
    @property
    def idSups(self):
        return self.__idSups
        
    @idSups.setter
    def idSups(self, idSups):
        self.__idSups= idSups

        
