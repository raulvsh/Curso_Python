miTupla=("Juan", 13,1,1995,13)

print(miTupla)

miLista=list(miTupla)

print(miLista)

miTupla2=tuple(miLista)

print(miTupla2)
miLista.append(2)

print(miLista)

print ("Juan" in miTupla2)
print (miTupla2.count(13))