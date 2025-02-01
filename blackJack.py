import random

class Kart:
    def __init__(self, sembol, sayı):
        self.sayı = sayı
        self.sembol = sembol

    def __str__(self):
        return f"{self.sembol} {self.sayı}"

    def deger(self):
        if self.sayı in ["J", "Q", "K"]:
            return 10
        elif self.sayı == "A":
            return 11
        else:
            return int(self.sayı)

class Deste:
    def __init__(self):
        self.deste_listesi = []
        sayı_listesi = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        sembol_listesi = ["sinek", "kupa", "maça", "karo"]
        for i in sembol_listesi:
            for a in sayı_listesi:
                x = Kart(i, a)
                self.deste_listesi.append(x)

    def karistir(self):
        random.shuffle(self.deste_listesi)

    def kart_cek(self):
        if self.deste_listesi:
            return self.deste_listesi.pop()
        else:
            return "Destede kart kalmadı!"

class Oyuncu:
    def __init__(self, isim="Tony Montana"):
        self.isim = isim
        self.el = []
        self.puan = 0

    def kart_cek(self, deste):
        cekilen_kart = deste.kart_cek()
        self.el.append(cekilen_kart)
        return cekilen_kart

    def el_degeri(self):
        toplam = 0
        as_sayısı = 0
        for kart in self.el:
            deger = kart.deger()
            if deger == 11:
                as_sayısı += 1
            toplam += deger
        while toplam > 21 and as_sayısı > 0:
            toplam -= 10
            as_sayısı -= 1
        self.puan = toplam
        return toplam

class Krupiye(Oyuncu):
    pass

def oyunu_baslat():
    deste = Deste()
    deste.karistir()

    oyuncu_ismi1 = input("İsim girmek istiyormusunuz? (evet/hayır)")
    if oyuncu_ismi1 == "evet":
        oyuncu_ismi2 = input("İsim girin ozaman!")
        oyuncu = Oyuncu(isim=oyuncu_ismi2)
    else:
        oyuncu = Oyuncu(isim="Tony Montana")
    krupiye = Krupiye()

    oyuncu.kart_cek(deste)
    oyuncu.kart_cek(deste)
    krupiye.kart_cek(deste)
    krupiye.kart_cek(deste)
    krupiye.el_degeri()
    print(f"{oyuncu.isim} kartları: {[str(kart) for kart in oyuncu.el]} (Toplam: {oyuncu.el_degeri()})")
    print(f"Krupiyenin açık kartı: {krupiye.el[0]}")

    if oyuncu.el_degeri() == 21:
        print("Blackjack! Tebrikler, kazandınız!")
        return

    double_yapti = False
    while oyuncu.puan < 21:
        if not double_yapti:
            double = input("Double? (evet/hayır): ")
            if double.lower() == "evet":
                oyuncu.kart_cek(deste)
                print(f"{oyuncu.isim} kartları: {[str(kart) for kart in oyuncu.el]} (Toplam: {oyuncu.el_degeri()})")
                double_yapti = True
                break
            elif double.lower() == "hayır":
                double_yapti = True
        devam = input("Kart çekelim mi? (evet/hayır): ")
        if devam.lower() == "evet":
            oyuncu.kart_cek(deste)
            print(f"{oyuncu.isim} kartları: {[str(kart) for kart in oyuncu.el]} (Toplam: {oyuncu.el_degeri()})")
        else:
            break

    if oyuncu.puan > 21:
        print("Bust! Krupiye kazandı.")
        return

    print(f"Krupiyenin kartları: {[str(kart) for kart in krupiye.el]} (Toplam: {krupiye.el_degeri()})")

    while krupiye.el_degeri() < 17:
        krupiye.kart_cek(deste)
        print(f"Krupiye kart çekti: {krupiye.el[-1]}")
        print(f"Krupiyenin kartları: {[str(kart) for kart in krupiye.el]} (Toplam: {krupiye.el_degeri()})")

    if krupiye.puan > 21:
        print("Krupiye bust! Oyuncu kazandı.")
    elif krupiye.puan > oyuncu.puan:
        print("Krupiye kazandı.")
    elif krupiye.puan < oyuncu.puan:
        print("Oyuncu kazandı.")
    else:
        print("Berabere!")

oyunu_baslat()







