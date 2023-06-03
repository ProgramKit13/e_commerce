class AdminPreferences:
    def __init__(self, productsPerPage, tokenUser):
        self.productsPerPage = productsPerPage
        self.tokenUser = tokenUser

    @property
    def productsPerPage(self):
        return self.__productsPerPage   
    @productsPerPage.setter
    def productsPerPage(self, productsPerPage):
        self.__productsPerPage = productsPerPage

    @property
    def tokenUser(self):
        return self.__tokenUser  
    @tokenUser.setter
    def tokenUser(self, tokenUser):
        self.__tokenUser = tokenUser

