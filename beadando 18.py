def torespont (szam):
    lista = []
    szam2=szam
    for i in (str(szam)):
        lista.append(szam%10)
        szam=szam//10
    lista=lista[::-1]
    for j in range (len(lista)):
        lista[j]=int(lista[j])
    for k in range (1,len(lista)):
        osszeg1 = 0
        osszeg2 = 0
        for i in range (0,k):
            osszeg1=osszeg1+lista[i]
        for j in range (k,len(lista)):
            osszeg2=osszeg2+lista[j]
        if osszeg1==osszeg2:
            szam2=str(szam2)
            return (szam2[:k]+"|"+szam2[k:])
    return False
print (torespont(336))
#pld. szam=336   ^^^
