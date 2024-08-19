import random

def tas_kagit_makas_tesnim_dede():
    while True:
        oyuncu_galibiyet_sayisi = 0
        bilgisayar_galibiyet_sayisi = 0
        tur_sayisi = 0

        while oyuncu_galibiyet_sayisi < 2 and bilgisayar_galibiyet_sayisi < 2:
            secenekler = ["taş", "kagit", "makas"]
            secim_oyuncu = input("Taş, kagit veya makas seç: ")

            while secim_oyuncu not in secenekler:
                print("Yanliş seçim yaptiniz! Lütfen taş, kagit veya makas seçiniz.")
                secim_oyuncu = input("Taş, kagit veya makas seç: ")
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarin seçimi: {bilgisayar_secimi}")

            if secim_oyuncu == bilgisayar_secimi:
                print("Berabere!")
            elif (bilgisayar_secimi == "kagit" and secim_oyuncu == "taş") or \
                 (bilgisayar_secimi == "makas" and secim_oyuncu == "kagit") or \
                 (bilgisayar_secimi == "taş" and secim_oyuncu == "makas"):
                print(f"Tur sonucu: Kaybettiniz! (Tur {tur_sayisi + 1})")
                bilgisayar_galibiyet_sayisi += 1
            else:
                oyuncu_galibiyet_sayisi += 1
                print(f"Tur sonucu: Kazandınız! (Tur {tur_sayisi + 1})")

            tur_sayisi += 1

        if oyuncu_galibiyet_sayisi == 2:
            print("Oyun bitti! Tebrikler, genel galip sizsiniz!")
        else:
            print("Oyun bitti! Üzgünüm, bilgisayar kazandı.")

        devam_mi_oyuncu = input("Devam etmek istiyor musunuz? (evet/hayır): ")
        devam_mi_bilgisayar = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın kararı: {devam_mi_bilgisayar}")

        if devam_mi_oyuncu == "hayır" or devam_mi_bilgisayar == "hayır":
            print("Oyun sona erdi.")
            break

tas_kagit_makas_tesnim_dede()
