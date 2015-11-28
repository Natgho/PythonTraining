#standart kullanıcı adı alma
kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız : ")

#kullanıcı uzunluklarını topluyorum.
toplam_uzunluk = len(kullanıcı_adı) + len(parola)

#süslü parantez yaptığım yer değişkenin geleceği yer oldu artık.
mesaj = "Kullanıcı adınız ve şifreniz {} karakterden oluşmaktadır."

#süslü parantezin içine koyacağım değer format metoduyla yapıyorum.
print(mesaj.format(toplam_uzunluk))

