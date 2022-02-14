'''
1.2 Feladat
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót: egy szavakat tartalmazó lista elemeiből generál egy másik listát, amelyben az eredeti szavak csupa nagybetűs formában szerepelnek! A program írja ki az eredeti és a generált listát is a képernyőre!
'''

lista = ['alma','kutya','fa']
lista2 = [szo.upper()for szo in lista]
print(lista)
print(lista2)