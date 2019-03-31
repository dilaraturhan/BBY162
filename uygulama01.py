""""
5 soruluk basit test uygulaaması
"""
print ("*** Merhaba, Sürealizm'i ne kadar biliyorsun? ***")
print ("Aşağıdaki sorulara 'D'ya da 'Y' ile cevap ver !")
print ("-----------------------------------------------")
sorular = [' Sürrealizm akımı 1924 \tte ortaya çıkmıştır  {D/Y}',
           ' Andre ve Pluton sürrealizm akımının önemli temsilcilerinden değildir {D/Y}',
           ' Sürealizm , gerçeküstücülük demektir {D/Y}',
           ' Orhan Veli bu akımı benimsemiştir {D/Y}',
           ' Sürealizme göre akıl ve mantık değersizdir {D/Y}', ]
cevaplar = [ 'D', 'Y', 'D' ,'D', 'D']
puan = 0
#Soru 1
cevap = input ((sorular [0]))
if cevaplar [0] == cevap.upper():
    print ("Tebrikler , doğru bildiniz!")
    puan += 1
else :
    print ("Cevabınız doğru değildir!")
#Soru 2
cevap = input  ((sorular [1]))
if cevaplar [1] == cevap.upper() :
    print ("Tebrikler, doğru bildiniz!")
    puan += 1
else :
    print ("Cevabınız doğru değildir!")
#Soru 3
cevap = input ((sorular [2]))
if cevaplar [2] == cevap.upper() :
    print (" Tebrikler , doğru bildiniz!")
    puan += 1
else :
    print ("Cevabınız doğru değildir!")
#Soru 4
cevap = input ((sorular [3]))
if cevaplar [3] == cevap.upper() :
    print ("Tebrikler , doğru bildiniz!")
    puan += 1
else :
    print ("Cevabınız doğru değildir!")
#Soru5
cevap = input ((sorular [4]))
if cevaplar [4] == cevap.upper() :
    print ("Tebrikler, doğru bildiniz!")
    puan += 1
else :
    print ("Cevabınız doğru değildir!")
#Test Sonu
print ("Testi tamamladınız, aldığınız not: "+str(puan*20))

