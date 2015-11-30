# Kullanıcının eval fonksiyonuyla istenilen dışında işlemler yapmasını
# istemiyoruz. Bu nedenle kullanılabilecek karakterleri matematiksel
# Karakterlerle sınırlamak için bir karakter seti oluşturuyoruz.
izn_vrln_karktrlr="0123456789/*-+, "

# Devamlı işlem yapabilmek için while döngüsüne sokuyoruz.
# Döngü break gelmedikçe kırılmasın diye şart olarak direk true veriyoruz.
while True:
    islem=input("Lütfen yapma istediğiniz işlemi giriniz(Örnek: 2*9) çıkmak için q yazın.\n")
    if islem == "q":
        break
    for s in islem:
# Her karakteri kontrol ediyoruz.
        if s not in izn_vrln_karktrlr:
            print("lütfen farklı işlemler denemeyin.")
            break
# İşlem yapmak için kullanılan eval fonksiyonuyla matematiksel işlemi
# Gerçekleştirmesi için eval'i kullanıyoruz.
    hesap=eval(islem)
    print(hesap)