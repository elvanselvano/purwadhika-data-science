class Student():
  total_murid = 0
  total_umur = 0

  def __init__(self, nama, NIM, umur):
    self.nama = nama
    self.NIM = NIM
    self.umur = umur
    Student.add_student(umur)

  @classmethod
  def hitung_umur(cls):
    return cls.total_umur/cls.total_murid

  @classmethod
  def add_student(cls, umur):
    cls.total_murid += 1
    cls.total_umur += umur

students = []
students.append(Student("Arief", "10001", 21))
students.append(Student("Ariyanda", "10002", 23))
students.append(Student("Raihan", "10003", 20))
students.append(Student("Prissilia", "99999", 22))
students.append(Student("Farhan", "10004", 21))

for s in students:
  print("Nama Siswa Ini Adalah", s.nama, "Nomor Induk Siswanya Yaitu", s.NIM, "Dan Umurnya Adalah", str(s.umur), "Tahun.")

print("Rata-rata Umur Siswa Di Kelas Ini Adalah", Student.hitung_umur())
