#Hatali olma olasiligi olan kisimlari try blogu icerisine yaziyoruz.
try:
    dosya = open("dosyaadı", "r")

# Dosya okuma hatasi olursa program sonlanmak yerine bu kisimdaki islemleri uygulayip devam ediyor.
except IOError:
    print("bir hata oluştu!")

#Beklenmedik hatalar olusma ihtimaline karsilik, tum hatalari yakalamk icin else kullaniliyor.
else:
    print("Olası diger hatalar icin...")

#Program patlasa dahi, mutlaka gerceklestirilmesi gereken islemleri finally bloguna yaziyoruz.
finally:
    dosya.close()

#Ozel bir hata firlatmak icin burayi kullaniyoruz. Bu sayede kisisel hatalar firlatabiliyoruz.
raise Exception("Bak buda hata, burada ayrica patlar program")
print("Buradaki deger hicbir zaman yazilmayacak cunku hata firlatip programi sonlandirmis olduk.")