
#1.soru
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print (metin [:20])

#2.soru
liste = ["Açık Bilim", "Açık Erişim" , "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste :
    print (i)

kelime = input("Bir kelime giriniz:")
kelimeler =["Elma","Salatalık" ]
sozluk = {"Elma": "Ağaçta yetişen bir tür meyve",
          "Salatalık": "Fidan üzerinde büyüyen bir tür sebze"}
if kelime in sozluk:
    if kelime ==("Elma"):
        print ("Ağaçta yetişen bir tür meyve")
    elif kelime ==("Salatalık"):
        print("Fidan üzerinde büyüyen bir tür sebze")
else:
    print(("Aradığınız sözcük kayıtlı değildir."))





