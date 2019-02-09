class Kendaraan():
    def __init__(self, name, fuel):
        self.name = name
        self.max_fuel = fuel # bisa ribuan Liter
        self.fuel = fuel
        self.traveled_distance = 0
        print("{} siap meluncur!".format(self.name))

    def go(self, distance):
        self.traveled_distance += distance
        print("{} telah bergerak sejauh {}.".format(self.name, distance))

    def refuel(self):
        self.fuel = self.max_fuel
        print("{} telah mengisi ulang bensinnya.".format(self.name))

    def horn(self):
        print("{} membunyikan klakson.".format(self.name))

    def __str__(self):
        if isinstance(self, Mobil) == True or isinstance(self, sepedaMotor)== True:
            return "{}\nBanyak sisa bensin: {}\nJarak yang ditempuh: {}\nBanyak penumpang: {}".format(self.name, self.fuel, self.traveled_distance, self.current_passenger)
        if isinstance(self, Truk) == True:
            return "{}\nBanyak sisa bensin: {}\nJarak yang ditempuh: {}\nBanyak penumpang: {}".format(self.name, self.fuel, self.traveled_distance, self.current_load)

class Mobil(Kendaraan):
    def __init__(self, name):
        super().__init__(name, 1000*len(name))
        self.max_passenger = len(name) + 1
        self.current_passenger = 1 # Driver

    def dropoff(self, num_of_drop_off):
        if self.current_passenger == 1:
            print("Tidak ada penumpang untuk diturunkan!")
        elif num_of_drop_off == (self.current_passenger - 1):
            self.current_passenger -= num_of_drop_off
            print("Penumpang di mobil {} sudah turun semua.".format(self.name))
        elif num_of_drop_off > (self.current_passenger - 1):
            self.current_passenger = 1
            print("Penumpang di mobil {} sudah turun semua.".format(self.name))
        else:
            self.current_passenger -= num_of_drop_off
            print("Penumpang di mobil {} turun sebanyak {}.".format(self.name, num_of_drop_off))

    def go(self, distance):
        self.fuel -= (self.current_passenger + len(self.name)) * distance
        super().go(distance)

    def addpassenger(self, num_of_passengers):
        if self.max_passenger == self.current_passenger:
            print("Kapasitas mobil {} sudah penuh.".format(self.name))
        elif num_of_passengers > (self.max_passenger - self.current_passenger):
            self.current_passenger += self.max_passenger - self.current_passenger
            print("Sejumlah {} orang naik ke mobil {} dan sebanyak {} ditinggalkan.".format((self.max_passenger - self.current_passenger), self.name, (num_of_passengers - (self.max_passenger - self.current_passenger))))
        else:
            self.current_passenger += num_of_passengers
            print("Sejumlah {} orang naik ke mobil {}.".format(num_of_passengers, self.name))

class sepedaMotor(Kendaraan):
    def __init__(self, name):
        super().__init__(name, 200*len(name))
        self.max_passenger = 2 # Kalo lebih nanti ditilang
        self.current_passenger = 1 # Driver

    def dropoff(self):
        if self.current_passenger > 1:
            self.current_passenger -= 1
            print("{} menurunkan penumpangnya.".format(self.name))
        else:
            print("{} tidak memiliki penumpang.".format(self.name))

    def go(self, distance):
        self.fuel -= (self.current_passenger * distance)
        super().go()

    def addpassenger(self):
        if self.current_passenger == 1:
            self.current_passenger += 1
            print("Penumpang naik ke motor {}.".format(self.name))
        else:
            print("Sepeda motor {} sudah ada penumpang.".format(self.name))


class Truk(Kendaraan):
    def __init__(self, name, weight):
        super().__init__(name, 7000*len(name))
        self.max_loads = 10*len(self.name)
        self.current_load = 0
        self.weight = weight

    def unload(self, num_of_unload):
        if self.current_load == 0:
            print("Truk {} tidak memiliki barang untuk diturunkan!".format(self.name))
        elif num_of_unload >= self.current_load:
            self.current_load = 0
            print("Barang sudah diturunkan semua dari truk {}.".format(self.name))
        else:
            self.current_load -= num_of_unload
            print("{} menurunkan barang sebanyak {}.".format(self.name, num_of_unload))

    def go(self, distance):
        self.fuel -= (self.current_load + len(self.name) + self.weight) * distance
        super().go(distance)

    def load(self, num_of_loads):
        if self.max_loads == self.current_load:
            print("Kapasitas truk {} sudah penuh!".format(self.name))
        elif num_of_loads > (self.max_loads - self.current_load):
            self.current_load += self.max_loads - self.current_load
            print("Truk {} menaikkan {} barang dan meninggalkan sejumlah {} barang.".format(self.name, (self.max_loads - self.current_load), (num_of_loads- (self.max_loads - self.current_load))))
        else:
            self.current_load += num_of_loads
            print("Truk {} menaikkan {} barang.".format(self.name, num_of_loads))


def main():
    keep_continue = True
    vehicles = {}
    while (keep_continue):
        current_input = input()
        current_input = current_input.lower()
        if current_input == 'sampai':
            for vehicle in vehicles:
                print(vehicles[vehicle])
            keep_continue = False
        else:
            command = current_input.split()
            if command[1] in vehicles:
                if len(command) == 2:
                    getattr(vehicles[command[1]], command[0])()
                else:
                    getattr(vehicles[command[1]], command[0])(int(command[2]))
            else:
                if command[0] == 'mobil':
                    vehicles[command[1]] = Mobil(command[1])
                if command[0] == 'sepedamotor':
                    vehicles[command[1]] = sepedaMotor(command[1])
                if command[0] == 'truk':
                    vehicles[command[1]] = Truk(command[1], int(command[2]))

if __name__ == '__main__':
    main()
