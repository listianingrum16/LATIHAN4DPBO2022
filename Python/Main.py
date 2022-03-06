from Driver import Driver
from Ship import Ship
from Airplane import Airplane

# deklarasi object untuk sub class driver, ship, dan airplane 
driver_obj = [Driver() for i in range(5)]
ship_obj = [Ship() for i in range(5)]
airplane_obj = [Airplane() for i in range(5)]

# memasukkan 5 data ke class person menggunakan setter 
driver_obj[0].setNik(1234567890000000)
driver_obj[0].setName("Byzantia Binar")
driver_obj[0].setGender("Perempuan")
driver_obj[1].setNik(1234567891111111)
driver_obj[1].setName("Yosua Henthreey Eden")
driver_obj[1].setGender("Laki - Laki")
driver_obj[2].setNik(1234567892222222)
driver_obj[2].setName("Vaden Javer")
driver_obj[2].setGender("Laki - Laki")
driver_obj[3].setNik(1234567893333333)
driver_obj[3].setName("Grizella Belinda")
driver_obj[3].setGender("Perempuan")
driver_obj[4].setNik(1234567894444444)
driver_obj[4].setName("Fannan Harshad")
driver_obj[4].setGender("Laki - Laki")

# menampilkan 5 data dari class person menggunakan getter
print("==================== Class Person ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - NIK : " + str(driver_obj[i].getNik()))
    print("   - Name : " + str(driver_obj[i].getName()))
    print("   - Gender : " + str(driver_obj[i].getGender()))

# memasukkan 5 data ke class job menggunakan setter 
driver_obj[0].setNip(987654321000000000)
driver_obj[0].setCompanyName("PT.Citilink Indonesia")
driver_obj[0].setPosition("Flight Operations Officer")
driver_obj[1].setNip(987654321011111111)
driver_obj[1].setCompanyName("PT.Samudera Indonesia Tbk.")
driver_obj[1].setPosition("Nahkoda")
driver_obj[2].setNip(987654321022222222)
driver_obj[2].setCompanyName("PT.Astra Internasional")
driver_obj[2].setPosition("Digital Acceleration Analyst")
driver_obj[3].setNip(987654321033333333)
driver_obj[3].setCompanyName("PT.Kereta Api Indonesia")
driver_obj[3].setPosition("Kondektur")
driver_obj[4].setNip(987654321044444444)
driver_obj[4].setCompanyName("PT.Garuda Indonesia")
driver_obj[4].setPosition("Pilot")

# menampilkan 5 data dari class job menggunakan getter
print("==================== Class Job ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - NIP : " + str(driver_obj[i].getNip()))
    print("   - Company Name : " + str(driver_obj[i].getCompanyName()))
    print("   - Position : " + str(driver_obj[i].getPosition()))

# memasukkan 5 data ke class driver menggunakan setter 
driver_obj[0].setLisenceId(101010100000)
driver_obj[0].setActiveUntil(2027)
driver_obj[0].setVehiclesType("Airplane")
driver_obj[1].setLisenceId(101010111111)
driver_obj[1].setActiveUntil(2023)
driver_obj[1].setVehiclesType("Bus")
driver_obj[2].setLisenceId(101010122222)
driver_obj[2].setActiveUntil(2025)
driver_obj[2].setVehiclesType("Ship")
driver_obj[3].setLisenceId(101010133333)
driver_obj[3].setActiveUntil(2022)
driver_obj[3].setVehiclesType("Car")
driver_obj[4].setLisenceId(101010144444)
driver_obj[4].setActiveUntil(2026)
driver_obj[4].setVehiclesType("Train")

# menampilkan 5 data dari class driver menggunakan getter
print("==================== Class Driver ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - Lisence ID : " + str(driver_obj[i].getLisenceId()))
    print("   - Active Until : " + str(driver_obj[i].getActiveUntil()))
    print("   - Vehicles Type : " + str(driver_obj[i].getVehiclesType()))

# memasukkan 5 data ke class vehicles menggunakan setter 
ship_obj[0].setFuelType("Aviation Gasoline")
airplane_obj[0].setMaxPassengers(360)
ship_obj[1].setFuelType("Bensin")
airplane_obj[1].setMaxPassengers(8)
ship_obj[2].setFuelType("Marine Fuel Oil")
airplane_obj[2].setMaxPassengers(500)
ship_obj[3].setFuelType("Aviation Turbine")
airplane_obj[3].setMaxPassengers(251)
ship_obj[4].setFuelType("Solar")
airplane_obj[4].setMaxPassengers(80)

# menampilkan 5 data dari class vehicles menggunakan getter
print("==================== Class Vehicles ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - Fuel Type : " + str(ship_obj[i].getFuelType()))
    print("   - Max Passengers : " + str(airplane_obj[i].getMaxPassengers()))

# memasukkan 5 data ke class ship menggunakan setter 
ship_obj[0].setAge(18)
ship_obj[0].setType("Labobar")
ship_obj[0].setCountryofManufacture("Germany")
ship_obj[1].setAge(5)
ship_obj[1].setType("Nowergian Joy")
ship_obj[1].setCountryofManufacture("Nowergia")
ship_obj[2].setAge(3)
ship_obj[2].setType("MSC Meraviglia")
ship_obj[2].setCountryofManufacture("Perancis")
ship_obj[3].setAge(7)
ship_obj[3].setType("Anthem of the Seas")
ship_obj[3].setCountryofManufacture("Germany")
ship_obj[4].setAge(6)
ship_obj[4].setType("Mutiara Sentosa III")
ship_obj[4].setCountryofManufacture("Germany")

# menampilkan 5 data dari class ship menggunakan getter
print("==================== Class Ship ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - Age : " + str(ship_obj[i].getAge()) + (" tahun"))
    print("   - Type : " + str(ship_obj[i].getType()))
    print("   - Country of Manufacture : " + str(ship_obj[i].getCountryofManufacture()))

# memasukkan 5 data ke class airplane menggunakan setter 
airplane_obj[0].setAge(30)
airplane_obj[0].setType("Airbus A330")
airplane_obj[0].setWingsLength(30.15)
airplane_obj[1].setAge(34)
airplane_obj[1].setType("ATR 72")
airplane_obj[1].setWingsLength(27.05)
airplane_obj[2].setAge(38)
airplane_obj[2].setType("Boeing 737")
airplane_obj[2].setWingsLength(28.9)
airplane_obj[3].setAge(34)
airplane_obj[3].setType("Airbus A320")
airplane_obj[3].setWingsLength(34.10)
airplane_obj[4].setAge(28)
airplane_obj[4].setType("Boeing 777")
airplane_obj[4].setWingsLength(32.40)

# menampilkan 5 data dari class airplane menggunakan getter
print("==================== Class Airplane ====================")
i = 0
for i in range(5):
    print("Data Ke-" + str(i+1))
    print("   - Age : " + str(airplane_obj[i].getAge()) + (" tahun"))
    print("   - Type : " + str(airplane_obj[i].getType()))
    print("   - Wings Length (m) : " + str(airplane_obj[i].getWingsLength()))

# menampilkan method keterangan class person dan class vehicles
print("===================== Keterangan =====================")
driver_obj[0].keteranganPerson()
ship_obj[0].keteranganVehiclesShip()
airplane_obj[0].keteranganVehiclesAirplane()
