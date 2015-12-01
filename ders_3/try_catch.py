sayi1= input("Lütfen bölme işlemi için bölünen değerini giriniz.")
sayi2= input("Lütfen bölen değeri giriniz.")

# Buradan sonra yapılacak işlemler tehlikeli olduğundan, buradan sonrasını
# Try bloğu içerisine alıyorum. Try bloğu içerisindeki kodlar çalışırken
# hata verdiğinde, python öncelikle except içerisinde bu hatanın yakalanıp
# yakalanmayacağını kontrol ediyor, yakalanıyorsa direk hatayı basmaktansa
# yazdığımız kodu çalıştırıyor.
try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)

# Sistemde tanımlı genel-geçer birkaç hata mevcut. ValueError int dönüştürme
# hatası gibi dönüştürme hatalarında ortaya çıkmaktadır. ZeroDivision ise adından
# anlaşılacağı gibi sıfıra bölme hatasıdır.

# "as" parametresi ile hatanın çıktısını yakalayıp istersek kullanıcıya hata
# metnini gösterebiliyoruz.
except (ValueError,ZeroDivisionError) as hata:
    print("Hatalı işlem. Hata sebebi:\n", hata)