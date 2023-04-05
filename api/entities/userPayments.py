from ..models import userPayments_model

class UserPayments():
    def __init__(self, userToken, cartToken, typePayment, value, status, datePayment, dateStatus, token):
        self.userToken = userToken
        self.cartToken = cartToken
        self.typePayment = typePayment
        self.value = value
        self.status = status
        self.datePayment = datePayment
        self.dateStatus = dateStatus
        self.token = token

    @property
    def userToken(self):
        return self.__userToken
    @userToken.setter
    def userToken(self, userToken):
        self.__userToken = userToken
    

    @property
    def cartToken(self):
        return self.__cartToken
    @cartToken.setter
    def cartToken(self, cartToken):
        self.__cartToken = cartToken
    

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
        self.__status = status

    @property
    def datePayment(self):
        return self.__datePayment
    @datePayment.setter
    def datePayment(self, datePayment):
        self.__datePayment = datePayment

    @property
    def dateStatus(self):
        return self.__dateStatus
    @dateStatus.setter
    def dateStatus(self, dateStatus):
        self.__dateStatus = dateStatus

    @property
    def token(self):
        return self.__token
    @token.setter
    def token(self, token):
        self.__token = token
