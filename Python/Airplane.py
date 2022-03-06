from Vehicles import Vehicles

class Airplane(Vehicles):

    # deklarasi atribut
    __age = 0
    __type = ""
    __wingsLength = 0

    # constructor
    def __init__(self, age = 0, type = "", wingsLength = 0):
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength
    
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

    # method set & get wingsLength
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    def getWingsLength(self):
        return self.__wingsLength