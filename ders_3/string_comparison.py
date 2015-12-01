# Programın amacı, iki farklı texti karşılaştırıp, içerisinde
# olmayan karakterleri ekrana yazdırmak.

ilk_metin="İlker_bu_konuda_elinden_geleni_yapiyor"

ikinci_metin="Bu_isin_bence_oluru_var"

# Karakterlerin tekrarlanmaması için bir string değişken oluşturuyoruz.

# Farklı karakterleri kontrol edebilmek için ara bir değişken oluşturuyoruz.
fark=""
for dgr in ilk_metin :

# Her karakterin 2. metinde geçip geçmediğini kontrol ediyoruz.
    if dgr not in ikinci_metin:
# Karakterin daha önce ara değere eklenip eklenmediğini kontrol ediyoruz.
        if dgr not in fark:
            fark+=dgr

print(*fark, sep=" ")


