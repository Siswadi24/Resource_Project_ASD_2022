from prettytable import PrettyTable
from pyrsistent import l

class JadwalPertandinganBola(object):
    def __init__(self, data):
        f = open(data, "r")
        self.jadwal = []
        for x in f.read().split('\n'):
            pecah = x.split(",")
            if len(pecah) > 1:
                self.jadwal.append({"No": pecah[0],"Match": pecah[1], "Venue": pecah[2], "Time": pecah[3] + pecah[4]})
    #urutkan data berdasarkan targetUrut dan urut
    def merge(self, targetUrut, urut, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            L[i] = self.jadwal[l + i]
        for j in range(0, n2):
            R[j] = self.jadwal[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if urut == "ASC":
                if L[i][targetUrut] <= R[j][targetUrut]:
                    self.jadwal[k] = L[i]
                    i += 1
                else:
                    self.jadwal[k] = R[j]
                    j += 1
            elif urut == "DESC":
                if L[i][targetUrut] >= R[j][targetUrut]:
                    self.jadwal[k] = L[i]
                    i += 1
                else:
                    self.jadwal[k] = R[j]
                    j += 1
            else:
                pass
            k += 1
        while i < n1:
            self.jadwal[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            self.jadwal[k] = R[j]
            j += 1
            k += 1

    def mergeSortPertandinganBola(self, targetUrut, urut, l, r):
        if l < r:
            # print(l, r)
            m = l + (r - l) // 2
            self.mergeSortPertandinganBola(targetUrut, urut, l, m)
            self.mergeSortPertandinganBola(targetUrut, urut, m + 1, r)
            self.merge(targetUrut, urut, l, m, r)


data = JadwalPertandinganBola("jadwalpertandinganpialadunia2018.csv")
# print("-------------------------------- Data sebelum diolah.CSV --------------------------------")
# tabel = PrettyTable(["No","Match", "Venue", "Time"])
# for x in data.jadwal:
#     tabel.add_row([x["No"],x["Match"], x["Venue"], x["Time"]])
# print(tabel)

# print("--------------------------------Mengurutkan data dari Waktu.CSV awal --------------------------------------")
# tabel = PrettyTable(["No" ,"Match", "Venue", "Time"])
# data.mergeSortPertandinganBola("Time", "ASC", 0, len(data.jadwal)-1)
# for x in data.jadwal:
#     tabel.add_row([x["No"] ,x["Match"], x["Venue"], x["Time"]])
# print(tabel)

# print("--------------------------------Mengurutkan data dari Waktu.CSV akhir --------------------------------------")
# tabel = PrettyTable(["No" ,"Match", "Venue", "Time"])
# data.mergeSortPertandinganBola("Time", "DESC", 0, len(data.jadwal)-1)
# for x in data.jadwal:
#     tabel.add_row([x["No"] ,x["Match"], x["Venue"], x["Time"]])
# print(tabel)


# print('--------------------------------Mengurutkan data dari Venue.CSV --------------------------------------')
# tabel = PrettyTable(["No" ,"Match", "Venue", "Time"])
# for x in data.mergeSortPertandinganBolaVenue("Venue","ASC"):
#     tabel.add_row([x["No"] ,x["Match"], x["Venue"], x["Time"]])
# print(tabel)





























































 # urutkan data dari waktu menggunakan merge sort
    # def mergeSortPertandinganBola(self, targetUrut ='' , urut="ASC", l, r):
    #     if len(self.jadwal) > 1:
    #         mid = len(self.jadwal) // 2
    #         L = JadwalPertandinganBola(data=self.jadwal[:mid])
    #         R = JadwalPertandinganBola(data=self.jadwal[mid:])

    #         L.mergeSortPertandinganBola(targetUrut, urut, l, r)
    #         R.mergeSortPertandinganBola(targetUrut, urut)
    #         self.mergeSortPertandinganBolaVenue(targetUrut, urut)

    #         for i in range(0, L):
    #             self.jadwal[i] = L.jadwal[i]
    #         for j in range(0, R):
    #             self.jadwal[j] = R.jadwal[j]
    #         i = 0
    #         j = 0
    #         k = 0
    #         while i < len(L) and j < len(R):
    #             if L.jadwal[i][targetUrut] <= R.jadwal[j][targetUrut]:
    #                 self.jadwal[k] = L.jadwal[i]
    #                 i += 1
    #             else:
    #                 self.jadwal[k] = R.jadwal[j]
    #                 j += 1
    #             k += 1
    #         while i < len(L):
    #             self.jadwal[k] = L.jadwal[i]
    #             i += 1
    #             k += 1
    #         while j < len(R):
    #             self.jadwal[k] = R.jadwal[j]
    #             j += 1
    #             k += 1
    #     return self.jadwal
    # #urutkan data dari venue menggunakan merge sort
    # def mergeSortPertandinganBolaVenue(self, targetUrut='', urut="ASC", l, r):
    #     if l < r:
    #         m = l + (r - l) // 2
    #         self.mergeSortPertandinganBolaVenue(targetUrut, urut, l, m)
    #         self.mergeSortPertandinganBolaVenue(targetUrut, urut, m + 1, r)
    #         self.mergeSortPertandinganBola(targetUrut, urut, l, m, r)
    # def __str__(self) :
    #     return str(self.jadwal)
