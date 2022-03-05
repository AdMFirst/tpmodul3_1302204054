class KodePos:
    """
    Insert fancy comment here, jk
    class KodePos, sesuai dengan dokumentasi yg
    ada di soal tp
    """
    data = {
        "Batununggal": "40266",
        "Kujangsari": "40287",
        "Mengger": "40267",
        "Wates": "40256",
        "Cijaura": "40287",
        "Jatisari": "40286",
        "Margasari": "40286",
        "Sekejati": "40286",
        "Kebonwaru": "40272",
        "Maleer": "40274",
        "Samoja": "40273"
        }

    def getKodePos(self, x):
        try:
            print(self.data[x])
        except:
            print("Kelurahan anda tidak ditemukan")

class DoorMachine:
    """
    Insert fancy comment here, jk
    class DoorMachine, sesuai dengan dokumentasi yg
    ada di soal tp
    """
    state = "Terkunci"

    def BukaPintu(self):
        if self.state == "Terkunci":
            self.state = "Terbuka"
            print("Pintu tidak terkunci")
        else:
            pass
    
    def KunciPintu(self):
        if self.state == "Terbuka":
            self.state = "Terkunci"
            print("Pintu terkunci")
        else:
            pass
    
    def CekKondisi(self):
        print(self.state)

if __name__ == '__main__':
    Kabupaten = KodePos()
    Kabupaten.getKodePos(input("Masukan kelurahan yang dicari :"))

    pintuRumah = DoorMachine()
    pintuRumah.CekKondisi()
    pintuRumah.BukaPintu()
    pintuRumah.KunciPintu()
