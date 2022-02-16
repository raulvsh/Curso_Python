miTupla = ("Juan", 13, 1, 1995)

print(miTupla)

miLista = list(miTupla)

print(miLista)

miTupla2 = tuple(miLista)

print(miTupla2)
miLista.append(2)

print(miLista)

print("Juan" in miTupla2)
print(miTupla2.count(13))


nombre, dia, mes, anyo = miTupla2
print("Nombre: " + nombre)
print("Dia " + str(dia))
print("Mes " + str(mes))
print("Anyo " + str(anyo))

print(miTupla2.index(13))
