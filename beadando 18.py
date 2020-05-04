lista=[]                                    #ures lista
szam=int(input("szam: "))
for i in (str(szam)):         
    lista.append(szam%10)                   #megjelenitjuk a listaban a szam 10-el valo maradekos osztasat (pld. 993; 3 -> lista)
    szam=szam//10                           #a szamrol le vagjuk az utolso egesz reszt (pld. 993; szam=99)
lista=lista[::-1]                           #vegul a listat megforditva megkapjuk a szamokat kulon-kulon (pld. "9","9","3")
for j in range (len(lista)):                #bejarjuk a lista hosszat
    lista[j]=int(lista[j])                  #egesz szamra alakitunk minden sztringet
