"""
18.04.2019
Dilara Turhan
"""
print("Sanatsal Adam Asmaca")
kullanıcı = input("Bir kullanıcı adı giriniz:")
print("Haydi başlayalım", kullanıcı, "!")

import random
kelimeListesi=("Dekolaj","Realizm","Portre","Eskiz","Tuval","Palet","Andre","silüet")
kelimeListesi = random.choice(["Dekolaj","Realizm","Portre","Eskiz","Tuval","Palet","Andre","silüet"])
kelimeListesi = kelimeListesi.upper()
canSayisi = 5
kelimeler = []
harfSayisi = "..."

for word in kelimeListesi:

    kelimeler.append(harfSayisi)

print(kelimeler)

while canSayisi > 0:

    i = 0

    tahmin = input("bir harf giriniz: ")
    tahmin = tahmin.upper()

    if tahmin in kelimeListesi:
        for kontrol in kelimeListesi:
            if kelimeListesi[i] == tahmin:
                kelimeler[i] = tahmin
            i += 1

        print("")
        print(kelimeler)
        print(" Bir tane \"%s\" harfi bulunuyor.   " %tahmin)


    else:
        canSayisi -= 1
        print("")
        print(kelimeler)
        print("  \"%s\" harfi kelimenin içinde yok. Lütfen başka harf giriniz" % tahmin)
        print(canSayisi, "Canınız Kaldı")


    if harfSayisi not in kelimeler:
        print("Tebrikler! Doğru bildiniz!")
        break

while canSayisi == 0:
    print("Maalesef bilemediniz!")
    print("Oyundan Çıkmak İstiyorsanız 'E' Tuşuna Basınız\nDevam Etmek İçin -> ENTER. ")
    devam = input(":")
    devam = devam.upper()
    if devam == "E":
        break
    else:
        continue
