class Product():
    def __init__(self, prodName, description, sector, supplier, supplierCode, manufacturer, valueResale, cust, tax, qt, discount, weight, weightUnit, dimensions, dimensionsUnit, barcode, datePurchase, lastUpdated, reorderPoint, restockTime, warrantyInfo, batchInfo, expiryDate, materialOrIngredients, safetyRating, shippingRestrictions, token):
        self.__prodName = prodName
        self.__description = description
        self.__sector = sector
        self.__supplier = supplier
        self.__supplierCode = supplierCode
        self.__manufacturer = manufacturer
        self.__valueResale = valueResale
        self.__cust = cust
        self.__tax = tax
        self.__qt = qt
        self.__discount = discount
        self.__weight = weight
        self.__weightUnit = weightUnit
        self.__dimensions = dimensions
        self.__dimensionsUnit = dimensionsUnit
        self.__barcode = barcode
        self.__datePurchase = datePurchase
        self.__lastUpdated = lastUpdated
        self.__reorderPoint = reorderPoint
        self.__restockTime = restockTime
        self.__warrantyInfo = warrantyInfo
        self.__batchInfo = batchInfo
        self.__expiryDate = expiryDate
        self.__materialOrIngredients = materialOrIngredients
        self.__safetyRating = safetyRating
        self.__shippingRestrictions = shippingRestrictions
        self.__token = token

    @property
    def prodName(self):
        return self.__prodName
        
    @prodName.setter
    def prodName(self, prodName):
        self.__prodName = prodName

    @property
    def description(self):
        return self.__description
        
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def sector(self):
        return self.__sector
        
    @sector.setter
    def sector(self, sector):
        self.__sector = sector

    @property
    def supplier(self):
        return self.__supplier
        
    @supplier.setter
    def supplier(self, supplier):
        self.__supplier = supplier

    @property
    def supplierCode(self):
        return self.__supplierCode
        
    @supplierCode.setter
    def supplierCode(self, supplierCode):
        self.__supplierCode = supplierCode

    @property
    def manufacturer(self):
        return self.__manufacturer
        
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

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
        self.__cust = cust

    @property
    def tax(self):
        return self.__tax
        
    @tax.setter
    def tax(self, tax):
        self.__tax = tax

    @property
    def qt(self):
        return self.__qt
        
    @qt.setter
    def qt(self, qt):
        self.__qt = qt

    @property
    def discount(self):
        return self.__discount
        
    @discount.setter
    def discount(self, discount):
        self.__discount = discount

    @property
    def weight(self):
        return self.__weight
        
    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def dimensions(self):
        return self.__dimensions
        
    @dimensions.setter
    def dimensions(self, dimensions):
        self.__dimensions = dimensions

    @property
    def datePurchase(self):
        return self.__datePurchase
        
    @datePurchase.setter
    def datePurchase(self, datePurchase):
        self.__datePurchase = datePurchase

    @property
    def lastUpdated(self):
        return self.__lastUpdated
        
    @lastUpdated.setter
    def lastUpdated(self, lastUpdated):
        self.__lastUpdated = lastUpdated

    @property
    def reorderPoint(self):
        return self.__reorderPoint
        
    @reorderPoint.setter
    def reorderPoint(self, reorderPoint):
        self.__reorderPoint = reorderPoint

    @property
    def restockTime(self):
        return self.__restockTime
        
    @restockTime.setter
    def restockTime(self, restockTime):
        self.__restockTime = restockTime

    @property
    def warrantyInfo(self):
        return self.__warrantyInfo
        
    @warrantyInfo.setter
    def warrantyInfo(self, warrantyInfo):
        self.__warrantyInfo = warrantyInfo

    @property
    def batchInfo(self):
        return self.__batchInfo
        
    @batchInfo.setter
    def batchInfo(self, batchInfo):
        self.__batchInfo = batchInfo

    @property
    def expiryDate(self):
        return self.__expiryDate
        
    @expiryDate.setter
    def expiryDate(self, expiryDate):
        self.__expiryDate = expiryDate

    @property
    def materialOrIngredients(self):
        return self.__materialOrIngredients
        
    @materialOrIngredients.setter
    def materialOrIngredients(self, materialOrIngredients):
        self.__materialOrIngredients = materialOrIngredients

    @property
    def safetyRating(self):
        return self.__safetyRating
        
    @safetyRating.setter
    def safetyRating(self, safetyRating):
        self.__safetyRating = safetyRating

    @property
    def shippingRestrictions(self):
        return self.__shippingRestrictions
        
    @shippingRestrictions.setter
    def shippingRestrictions(self, shippingRestrictions):
        self.__shippingRestrictions = shippingRestrictions

    @property
    def token(self):
        return self.__token
        
    @token.setter
    def token(self, token):
        self.__token = token

    @property
    def weightUnit(self):
        return self.__weightUnit
        
    @weightUnit.setter
    def weightUnit(self, weightUnit):
        self.__weightUnit = weightUnit

    @property
    def dimensionsUnit(self):
        return self.__dimensionsUnit
        
    @dimensionsUnit.setter
    def dimensionsUnit(self, dimensionsUnit):
        self.__dimensionsUnit = dimensionsUnit

    @property
    def barcode(self):
        return self.__barcode
        
    @barcode.setter
    def barcode(self, barcode):
        self.__barcode = barcode