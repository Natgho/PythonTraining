metin = "Bu metin gayet ilginc degisiklikleri gayet yasayacak."

#Metnin temel hali
print(metin)

#Metindeki gayet gecen yerleri degistiyoruz.
metin = metin.replace("gayet","ilginc")
print(metin)

#Metindeki ilginc gecen yerlerden sadece ilkini degistirmemizi sagliyor.
metin= metin.replace("ilginc","baya",1)
print(metin)

#metni bosluga göre parcalama islemi yapiyor.
parcala= metin.split()

print("\n\nDizi hali;")
print(parcala)


#metni "," karakterine gore parcaliyor.
metin = "Bu,metin,gayet,ilginc,degisiklikleri,gayet,yasayacak"
parcala = metin.split(",")
print(parcala)
