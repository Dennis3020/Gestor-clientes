import re
def leer_texto(min, max, mensaje= None):
    print(mensaje) if mensaje else None
    while True:
        texto = input('> ')
        if len(texto) >= min and len(texto) <= max:
            return texto

def validacion_dni(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in  lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente")
            return False
    return True