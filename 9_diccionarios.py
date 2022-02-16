miDiccionario = {"Alemania": "Berlin", "España": "Madrid",
                 "Francia": "París", "Reino Unido": "Londres"}

print(miDiccionario["Francia"])

miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

miDiccionario["Italia"] = "Roma"
print(miDiccionario)
del miDiccionario["Reino Unido"]
print(miDiccionario)


miTupla = ["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario2 = {miTupla[0]: "Madrid", miTupla[1]: "París",
                  miTupla[2]: "Londres", miTupla[3]: "Berlín"}

print(miDiccionario2)
print(miDiccionario2["España"])
print(miDiccionario2[miTupla[2]])
