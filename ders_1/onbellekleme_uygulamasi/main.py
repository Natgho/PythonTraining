# Sezer BOZKIR - 2015

# Python özelliği gereği bazı değerleri bellekte otomatik adreslemekte.
# Bunları görmek için ilk for ile 1-1000 arası sayıları çeviriyoruz
# 2. for dada bu değerleri başka şekilde oluşturulan 1-1000 arası sayıların
# id değerleri ile "is" operatörü ile karşılaştırıyoruz.

for k in range(-1000,1000) :
    for v in range(-1000,1000):
        if k is v:
            print(k)

# Normal bir string değerin daimi bir adresinin olmadığını görmek için deneme
print("String değerin id'si: ",id("bunun id'si ne olabilir"))