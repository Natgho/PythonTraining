# Açmak istediğim dosyayı seçiyorum, dosyayı ben burada direk ekledim, farklı
# Yerler için yolu ayrıca göstermek gerek.
d1 = open("icerik_1.txt")
# Dosyadaki her satırı 1 parça olarak kaydediyorum.
icerik_1 = d1.readlines()

#Karakter sayısını saymak için başlangıç değeri atıyorum.
sayi = 0

krkter = input("Lütfen aradığınız karakterin miktarını giriniz.")

# Her stringi tek tek ele alabilmek için 1. for da string setlerine ayırıyorum.
for met in icerik_1:
# Her string setinin içinde gezebilmek için 2. for döngüsüne sokuyorum.
    for harf in met:
        if krkter == harf:
            sayi+=1
print("{} karakteri, belirtilen metinde {} kere geçmekte.".format(krkter,sayi))

d1.close()