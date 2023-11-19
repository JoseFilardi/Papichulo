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

def validar_values_unique(email, username, id, list_user):
    for user in list_user:
        if user.email == email or user.username == username or user.id == id:
            return False
    
    return True

def validar_email_unique(email, list_user):
    for user in list_user:
        if user.email == email:
            return False
    
    return True

def validar_username_unique(username, list_user):
    for user in list_user:
        if user.username == username:
            return False
    
    return True

#Validar que un string solo contenga letras
def validar_letras(string):
    while not string.isalpha() or len(string) == 0:
        print("Error!!! Dato Inválido.")
        string = input("\nIngrese su nombre: ")

#Validar 
def validar_cedula(cedula):
    pass