# 3 kere parola oluşturma hakkı vermek istiyorum, range 3 ile başlayıp
# 0 değerine gelene kadar çalıştırıyorum.
for i in range(3,0,-1):
    parola=input("Lütfen parola belirleyin:")

# Eğer kullanıcı parola kısmını boş bıraktıysa işlemi görmezden geliyorum.
# Pass ifadesi o işlemi görmezden gelmemi sağlıyor.
    if not parola:
        pass

# Parolanın aralığını range ile belirliyorum. Döngüyü kırmak içinde break
# İfadesini kullanıyorum
    elif len(parola) in range(3,8):
        print("Parolanı oluşturuldu. Yeni parola;", parola)
        break
    elif len(parola) not in range(3,8):
        print("Parola en az 3 en fazla 8 karakterden oluşmalıdır.")

# Kullanıcının hakkı kalmamışsa, 0 hakkı kaldığını belirtmek istemediğimden
# Continue deyimiyle print satırını pas geçip döngünün bitmesini sağlıyorum.
    if i == 1:
        continue
    print("Parola oluşturmak için {} hakkınız kaldı.".format(i-1))

