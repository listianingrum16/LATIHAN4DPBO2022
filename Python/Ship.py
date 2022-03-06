from Vehicles import Vehicles

class Ship(Vehicles):

    # deklarasi atribut
    __age = 0
    __type = ""
    __countryofManufacture = ""

    # constructor
    def __init__(self, age = 0, type = "", countryofManufacture = ""):
        self.__age = age
        self.__type = type
        self.__countryofManufacture = countryofManufacture
    
    # method set & get age
    def setAge(self, age):
        self.__age = age
    def getAge(self):
        return self.__age

    # method set & get type
    def setType(self, type):
        self.__type = type
    def getType(self):
        return self.__type

    # method set & get cuntryofManufacture
    def setCountryofManufacture(self, countryofManufacture):
        self.__countryofManufacture = countryofManufacture
    def getCountryofManufacture(self):
        return self.__countryofManufacture