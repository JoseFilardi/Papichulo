#Validar un correo
def validar_email(email):
    if email.count('@') == 1:
        if email[0] == "@":
            print("El correo no puede empezar con '@'.")
            return -1
        else:
            partes_email = email.split("@")
            if partes_email[1] == "unimet.edu.ve" or partes_email[1] == "correo.unimet.edu.ve":
                return 1
            else:
                print("Los correos solo pueden ser de los siguientes dominios: 'unimet.edu.ve' o 'correo.unimet.edu.ve' ")
                return -1
    else:
        print("El correo debe contener al menos un '@'.")
        return -1

#Validar que un string solo contenga letras
def validar_letras(string):
    while not string.isalpha() or len(string) == 0:
        print("Error!!! Dato Inválido.")
        string = input("\nIngrese su nombre: ")

#Validar 
def validar_option(num1, num2, option):
    while (not option.isnumeric()) or (not int(option) in range(num1, num2+1)):
        print("Opción no válida.")
        option = input("\nIngrese la opcion: ")

def validar_cedula(cedula):
    pass