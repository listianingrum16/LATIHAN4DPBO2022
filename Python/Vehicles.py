class Vehicles():

    # deklarasi atribut
    __fuelType = ""
    __maxPassengers = 0

    # constructor
    def __init__(self, fuelType = "", maxPassengers = 0):
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
    
    # method set & get fuel type
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    def getFuelType(self):
        return self.__fuelType

    # method set & get max passengers
    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    # method untuk menampilkan keteragan tambahan
    def keteranganVehiclesShip(self):
        print("Class Vehicles merupakan parent dari class Ship.")
    def keteranganVehiclesAirplane(self):
        print("Class Vehicles merupakan parent dari class Airplane.")
    