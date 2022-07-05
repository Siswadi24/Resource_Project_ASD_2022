class jadwalPertandingan(object):
    def __init__(self,data=""):
        f = open(data,"r")
        self.jadwal = []
        for x in f.read().split("\n"):
            obj = x.split(",") 
            if len(obj)>1:
                self.jadwal.append({'pertandingan':obj[1], 'tempat':obj[2], 'waktu':obj[3] + obj[4]})

class Stack():
    _data = list()
    _pertandingan = []

    def isEmpty(self):
        return len(self.jadwal) == 0

    def push(self, item):
        pertandingan = item.split(",")[0]
        
        if pertandingan not in self._pertandingan:
            self._pertandingan.append(pertandingan)
            self._data.append(item)

    def pop(self):
        item = self._data.pop(-1)
        return item

s = Stack()
f = open("jadwalpertandinganpialadunia2018.csv").read().split("\n")

for i in f:
    s.push(i)

for i in range(len(s._data)):
    print(s.pop())




          
