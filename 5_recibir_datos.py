def recibir_datos():
    return input("Introduzca su nombre: ")

def saludo(nombre):
    print("Buenos días " + nombre)
    
nombre = recibir_datos()

saludo(nombre)