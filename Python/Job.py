from Person import Person

class Job(Person):

    # deklarasi atribut
    __nip = 0
    __companyName = ""
    __position = ""

    # constructor
    def __init__(self, nip = 0, companyName = "", position = ""):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position
    
    # method set & get nip
    def setNip(self, nip):
        self.__nip = nip
    def getNip(self):
        return self.__nip

    # method set & get company name
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    def getCompanyName(self):
        return self.__companyName

    # method set & get position
    def setPosition(self, position):
        self.__position = position
    def getPosition(self):
        return self.__position    