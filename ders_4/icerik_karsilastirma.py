dosya1= open("icerik_1.txt",encoding="utf-8")
#dosya1 degiskeni icerisine icerik1'i aciyoruz, karakterleri dogru alabilmesi icin utf-8 ile acmasını belirtiyoruz.

dosya1_icerik= str(dosya1.readlines())
#actiginde tur olarak list yapisinda geldiginden, karsilasirma yapabilmek icin onu string'e konver edebilmek
#icin donucum yapiyoruz. (str ile)

dosya1.close()
#dosya ile isimiz bittigine gore kapatiyoruz, yalniz dikkat, bunu unutmamiz, dosyayi tekrar kullanmak istedigimizde
#problem olusturacagindan, mumkun mertebe isimiz bitince kapatin.

dosya2 = open("icerik_2.txt",encoding="utf-8")
dosya2_icerik = str(dosya2.readlines())
dosya2.close()
print(dosya1_icerik)
print(dosya2_icerik)

print("Karsilastirma yapiliyor...")
for icerik in dosya1_icerik :
    #Her karakteri tek tek string icerisinde ariyoruz, olmamasi durumunda bu bloga giriyor.
    if not icerik in dosya2_icerik:
        print(icerik,end="")

