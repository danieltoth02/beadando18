lista=[]
szam=int(input("szam: "))
for i in (str(szam)):
    lista.append(szam%10)
    szam=szam//10                         
lista=lista[::-1]                         
for j in range (len(lista)):            
    lista[j]=int(lista[j])                
