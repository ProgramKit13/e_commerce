class AdminPreferences:
    def __init__(self, productsPerPage, suppliersPerPage, tokenUser):
        self.productsPerPage = productsPerPage
        self.tokenUser = tokenUser
        self.suppliersPerPage = suppliersPerPage

    @property
    def productsPerPage(self):
        return self.__productsPerPage   
    @productsPerPage.setter
    def productsPerPage(self, productsPerPage):
        self.__productsPerPage = productsPerPage

    @property
    def suppliersPerPage(self):
        return self.__suppliersPerPage
    @suppliersPerPage.setter
    def suppliersPerPage(self, suppliersPerPage):
        self.__suppliersPerPage = suppliersPerPage
        

    @property
    def tokenUser(self):
        return self.__tokenUser  
    @tokenUser.setter
    def tokenUser(self, tokenUser):
        self.__tokenUser = tokenUser


