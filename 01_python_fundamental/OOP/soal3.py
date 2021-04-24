class Kendaraan():
  def __init__(self, capacity, distance):
    self.capacity = capacity
    self.distance = distance

  def price(self):
    return self.capacity * self.distance * 100

class Bus(Kendaraan):
  def bus_price(self):
    return round(Kendaraan.price(self) * 1.1, 2)

distance = int(input("Jarak Tempuh : "))
capacity = int(input("Kapasitas Kendaraan : "))
b = Bus(distance, capacity)
print("Tarif Bus Sekolah Yang Harus di Bayar Adalah Rp", b.bus_price())