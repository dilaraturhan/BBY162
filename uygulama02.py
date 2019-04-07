"""
Dilara Turhan uygulama02.py
"""
print("* Bilgisayar bilginize ne kadar güveniyorsunuz? *")
print("5 soruda bilginizi değerlendirelim!")
print("..................................................")
sorular = ["PowerPoint’te hazır olarak gelen zemin deseni,yazı rengi ve tipleri gibi ayarlara ne denir?",\
           "Excel’de formüllerin başında Aşağıdakilerden hangisi kullanılır?",\
           "PowerPoint’ te slayt geçişi ayarlarını yapmak için hangi sıra takip edilmelidir ? ",\
           "Sayfaya satır eklemek için aşağıdakilerden hangisi kullanılmalıdır?",\
           "Aşağıdakilerden hangisi ekle menüsünden eklenmez?",]

cevaplar = ["B","C", "E", "A", "A"]
cevapA =["Zemin Taslağı ", "*", "Düzen-slayt geçişi", "Ekle-Satır", "Dosya" ]
cevapB =["Tasarım", "?", "Slayt Gösteri-Özel Animasyon-Slayt Geçişi", "Biçim-Sütun" ,"Satır"]
cevapC =["Slayt Düzeni", "=", "Ekle-Özel Animasyon-Slayt Geçişi", "Ekle-Yeni Sütun", "Grafik"]
cevapD =["Taslak", "%","Düzen-Özel Animasyon-Slayt Geçişi","Düzen-Sütun" ,"Köprü"]
cevapE =["Arka Plan", "/" ,"Slayt Düzeni-Slayt Geçişi" ,"Biçim-Sütun","Çizimler"]
puan =0
for i in range (len(sorular)):
    print("soru " + str(i+1)+":"+sorular[i])
    print("A " + cevapA[i])
    print("B " + cevapB[i])
    print("C " + cevapC[i])
    print("D " + cevapD[i])
    print("E " + cevapE[i])
    cevap = input("lütfen cevabınızı giriniz: ")
    if cevaplar[i] == cevap.upper():
       puan +=1
print("Testi bitirdiniz.")
print("Sonucunuz: "+ str(int((puan/len(sorular))*100)))

puan > 50
if puan >50:
    print("Waov, hiçte fena değilsiniz!")
else:
    print ("Kendinizi geliştirmelisiniz!")
