class Person():

    # deklarasi atribut
    __nik = 0
    __name = ""
    __gender = ""

    # constructor
    def __init__(self, nik = 0, name = "", gender = ""):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
    
    # method set & get nik
    def setNik(self, nik):
        self.__nik = nik
    def getNik(self):
        return self.__nik

    # method set & get name
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    # method set & get gender
    def setGender(self, gender):
        self.__gender = gender
    def getGender(self):
        return self.__gender
    
    # method untuk menampilkan keterangan tambahan
    def keteranganPerson(self):
        print("Class Person merupakan parent dari class Job.")