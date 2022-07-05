import pandas as pd                    
from prettytable import PrettyTable 

lok = 'D:\\menggabut\\Searching\\eksel.xlsx'
files = pd.ExcelFile(lok)                                                       
df = files.parse(files.sheet_names[0])                                      
list = df.to_dict()                                                             
data = []                                                                   
for index in range(0, len(list['Pertandingan / Match'])):                       
    kata = ''                                                                   
    posisi = 0                                                          
    for i in list:                                                              
        posisi += 1                                                             
        kata += str(list[i][index])                                             
        if posisi != len(list):                                         
            kata += '#'                                                         
    data.append(kata.split('#'))                                            
    
def cetakData(list):                                                            
    jadwalLama = PrettyTable(['No', 'Petandingan', 'Tempat', 'Tanggal', 'Waktu'])       
    for i in list:                                                              
        jadwalLama.add_row(i)                                                   
    print(jadwalLama)

def cariTempat(tempat):
    x = []
    for i in data:
        if tempat == i[2]:
            x.append(i)
    hasil = PrettyTable(['No', 'Petandingan', 'Tempat', 'Tanggal', 'Waktu'])
    for i in x:
        hasil.add_row(i)
    print(hasil)
    print("Kondisi :")
    if len(x) > 0:
        return True
    else:
        return False

def cariTanggal(tanggal):
    y = []
    for i in data:
        if tanggal == i[3]:
            y.append(i)
    hasil = PrettyTable(['No', 'Petandingan', 'Tempat', 'Tanggal', 'Waktu'])
    for i in y:
        hasil.add_row(i)
    print(hasil)
    print("Kondisi :")
    if len(y) > 0:
        return True
    else:
        return False

##cetakData(data)
cariTempat('Saransk')
cariTanggal('2018-06-21 00:00:00')
