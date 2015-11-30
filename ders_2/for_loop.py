harfler="Sezer Bozkır\n"

# in ile yazıldığında harfler bir karakter dizisi oldğundan harf
# değişkeni içerisine her seferinde 1 karakteri yazarak ekrana bastırmayı
# sağlıyor.
for harf in harfler:
    print(harf, end="")



# Kullanılmamasını istediğimiz türkçe karakterleri yazıyoruz.
tr_karakterler="şçöğüİı"
parola=input("Lütfen parolanızı giriniz\n")
# hata kontrolü için bir hata değişkeni oluşturuyoruz.
err=0

# Parolanın girildiğinin kontrolünü yapıyoruz.
if not parola:
        print("Parola yazmak zorundasınız")
        err=1
# Parolanın her karakterini tek tek incelemek için bir for döngüsü oluşturuyoruz.
for karakter in parola:

# Eğer karakterin içerisinde türkçe karakter varsa uyarı veriyoruz.
    if karakter in tr_karakterler:
        print("Parola içerisinde türkçe karakter kullanılamaz")
# Hata durumunu kontrol etmek için err değişkenini 1 yapıyoruz.
# Döngüden çıkıyoruz.
        err=1
        break
# Hata durumunu son kez kontrol edip parolayı onaylıyoruz.
if err==0:
    print("\nParolanız onaylandı")