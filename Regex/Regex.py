import pandas as pd                    
from prettytable import PrettyTable 
import re                           

lok = 'D:\\Kuliah\\Teknik Informatika\\Semester 4\\Praktikum Algoritma Struktur Data\\Latihan\\FinalProject\\WorldCupTimetable2018.xlsx'
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
    jadwalLama = PrettyTable(['No', 'Petandingan', 'Tempat', 'Waktu'])          
    for i in list:                                                              
        jadwalLama.add_row(i)                                                   
    print(jadwalLama)                                                           

## a). Menghitung banyaknya kecocokan yang terjadi di suatu tempat diawali dengan huruf tertentu.
def JumlahPertandinganTempat(tempat):                                                   
    print("Mengecek Jumlah Pertandingan di Tempat dengan awalan huruf/kata :", tempat)  
    banyak = {}                                                                         
    pola = r"%s.*"%tempat.lower()                                                       
    for i in data:                                                                      
        if re.match(pola, i[2].lower()):                                                
            if i[2] in banyak:                                                          
                banyak[i[2]] += 1                                           
            else:                                                                       
                banyak[i[2]] = 1                                
    hasil = PrettyTable(["Tempat","Banyak Pertandingan"])                           
    for i in banyak:                                                                    
        hasil.add_row([i, banyak[i]])                                                   
    print(hasil)#mencetak tabel hasil

## b). Menghitung berapa kali setiap negara memainkan pertandingan.
def JumlahNegaraBertanding():                               
    print("Mengecek Jumlah Negara Bertanding :")            
    huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                
    banyak = {}                                             
    for negara in huruf:                                
        pola = "%s\w+"%negara                               
        for i in data:                                      
            if re.findall(pola, i[1]):                      
                key = ''                                
                if key.join(re.findall(pola, i[1])) not in banyak:      
                    banyak[key.join(re.findall(pola, i[1]))] = 1    
                else:                                                   
                    banyak[key.join(re.findall(pola, i[1]))] += 1
    hasil = PrettyTable(["Negara", "Banyak Pertandingan"])              
    for i in banyak:                                                    
        hasil.add_row([i, banyak[i]])                                   
    print(hasil)                                                

