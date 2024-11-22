#Crear la función que valida la contraseña
def validar_contraseña(contraseña:str):
    #Crear lista de dígitos permitidos
    simbolos_especiales = "@#$% "


    if len(contraseña) < 8: #Validar el largo de la contraseña
        raise ValueError("La contraseña no cumple con los criterios establecidos.")

    #Declarar varialbes que validan si se cumple el críterio o no
    mayusculas = False
    minusculas = False
    numero = False
    simbolo = False

    #Validar cada simbolo en contraseña
    for letra in contraseña:
        if letra.islower(): #Validar si tiene minusculas
            minusculas = True
        if letra.isupper():#Validar si tiene mayusculas
            mayusculas = True
        if letra.isdigit(): #Validar si tiene números
            numero = True
    if not contraseña.isalnum(): # Validar si tiene dígitos
        simbolo = True

    #Validar si cumple con todos los críterios
    cumple = [mayusculas,minusculas,numero,simbolo]
    if False in cumple:
        raise ValueError("La contraseña no cumple con los criterios establecidos.")
        return ValueError
    else:
        return True



"""Examples"""
contraseña = "contraseña1@"

try:
    if validar_contraseña(contraseña):
        print("¡La contraseña es segura!")
except ValueError as error:
    print(error)

contraseña = "#S53uJQysbyz(wpT"
try:
    if validar_contraseña(contraseña):
        print("¡La contraseña es segura!")
except ValueError as error:
    print(error)
