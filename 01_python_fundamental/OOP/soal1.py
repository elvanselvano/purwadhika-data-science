class Persegi():
  def __init__(self, sisi):
    self.sisi = sisi
  
  def keliling(self):
    return self.sisi * 4

  def luas(self):
    return self.sisi ** 2

sisi = int(input("Masukkan Sisi Persegi: "))
p = Persegi(sisi)
print(p.keliling())
print(p.luas())