from prettytable import PrettyTable

class jadwalPertandingan(object):
    def __init__(self,data=""):
        f = open(data,"r")
        self.jadwal = []
        for x in f.read().split("\n"):
            obj = x.split(",")
            if len(obj)>1:
                self.jadwal.append({'pertandingan':obj[1], 'tempat':obj[2], 'waktu':obj[3] + obj[4]})
                
    def mergeshort(self,targeturut="",urut="ASC") -> list:
        for i in range(len(self.jadwal)):
            n = i
            for j in range(i+1, len(self.jadwal)):
                if urut == "ASC":
                    if self.jadwal[n][targeturut] > self.jadwal[j][targeturut]:
                        n = j
                else:
                    if self.jadwal[n][targeturut] < self.jadwal[j][targeturut]:
                        n = j
            self.jadwal[i], self.jadwal[n] = self.jadwal[n], self.jadwal[i]
        return self.jadwal
        
            
    # def __str__(self) -> str:
    #     tampil = ""
    #     tampil +="----------------------------------------------------------------------\n"
    #     for x in self.jadwal:
    #         tampil += x["pertandingan"] + " di " +x["tempat"] + " pada " + x["waktu"] + "\n"
    #     return tampil

('------------------------------------ Mengeluarkan data dari csv ----------------------------------')
data = jadwalPertandingan("jadwalpertandinganpialadunia2018.csv")
print("-------------------------------- Data sebelum diolah.CSV --------------------------------") 
tabel = PrettyTable(["Match", "Venue", "Time"])
for x in data.jadwal:
    tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"]])
print(tabel)

# print('--------------------------------Mengurutkan data dari Waktu.CSV --------------------------------------')
# tabel = PrettyTable(["Match", "Venue", "Time"])
# for x in data.mergeshort("waktu","ASC"):
#     tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"]])
# print(tabel)

# print('--------------------------------Mengurutkan data dari Venue.CSV --------------------------------------')
# tabel = PrettyTable(["Match", "Venue", "Time"])
# for x in data.mergeshort("tempat","ASC"):
#     tabel.add_row([x["pertandingan"], x["tempat"], x["waktu"]])
# print(tabel)



# print(data.jadwal)  # menampilkan datarray sebelum diolah
# print()
# print("Nama tempat pertandingan Ascending")
# data.mergeshort("tempat")
# print(data)
# print("Nama tempat pertandingan Descending")
# data.mergeshort("tempat","DESC")
# print(data)
# print("Waktu pertandingan Ascending")
# data.mergeshort("waktu")
# print(data)
# print("Waktu pertandingan Descending")
# data.mergeshort("waktu","DESC")
# print(data)