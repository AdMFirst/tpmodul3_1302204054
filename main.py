class KodePos:
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

if __name__ == '__main__':
    Kabupaten = KodePos()
    Kabupaten.getKodePos(input("Masukan kelurahan yang dicari :"))
    Kabupaten.getKodePos("Maleer")
    Kabupaten.getKodePos("Bojongsoang")