from Job import Job

class Driver(Job):

    # deklarasi atribut
    __lisenceId = 0
    __activeUntil = 0
    __vehiclesType = ""

    # constructor
    def __init__(self, lisenceId = 0, activeUntil = 0, vehiclesType = ""):
        self.__lisenceId = lisenceId
        self.__activeUntil = activeUntil
        self.__vehiclesType = vehiclesType
    
    # method set & get lisence id
    def setLisenceId(self, lisenceId):
        self.__lisenceId = lisenceId
    def getLisenceId(self):
        return self.__lisenceId

    # method set & get active until
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    def getActiveUntil(self):
        return self.__activeUntil

    # method set & get vehicles type
    def setVehiclesType(self, vehiclesType):
        self.__vehiclesType = vehiclesType
    def getVehiclesType(self):
        return self.__vehiclesType