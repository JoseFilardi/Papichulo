import requests
from Estudiante import Estudiante
from Profesor import Profesor
from Post import Post

class App:
    
    def __init__(self):
        self.list_post = []
        self.list_user = []


    def api(self):
        link="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json"
        responce = requests.get(link)
        datos = responce.json()
        print(datos)
                
#-----------------------------------------------------------------------------------  
    def login(self):
        while True:
            
            print("""       ===========================     
                            |~|  M E T R O G R A M  |~|
                            ===========================
      
                        ===================================
                        |1|       Inicio de Sesión      |1|
                        ===================================

                           =============================
                           |2|        Registro       |2|
                           =============================
              
              
            ================
            |3|  Salir   |3|
            ================  
            """)
            
            opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion.isnumeric()) or (not int(opcion) in range(1,4)):
                print("Error!!! Dato Inválido.")
                opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                
            if opcion == "1":
                self.inicio
            elif opcion == "2":
                self.registrar_user
            elif opcion == "3":
                 break
    
    def inicio(self):
        while True:
            username = input("Ingrese su username: ")
            email = input("Ingrese su correo: ")
            
             
    def registrar_user(self):
        
        # Pedir información al usuario
        nombre = input("\nIngrese su nombre: ")
        while not nombre.isalpha() or len(nombre) == 0:
          print("Error!!! Dato Inválido.")
          nombre = input("\nIngrese su nombre: ")

        apellido = input("Ingrese su apellido: ")
        while not apellido.isalpha() or len(apellido) == 0:
          print("Error!!! Dato Inválido.")
          apellido = input("\nIngrese su nombre: ")

        while True:
            email = input("Ingrese su correo electrónico: ")
            if "@" in email:
                dominio = email.split("@")
                if not email.count("@") == 1 and not dominio[1]=="correo.unimet.edu.ve" :
                    print("El correo electrónico no tiene el formato correcto.")
                    break
                else:
                    print("El correo electrónico es válido.")
                    break
            else:
                print("El correo electrónico no tiene el formato correcto.")

        username = input("Ingrese su nombre de usuario: ")

        # Mostrar opciones para Carrera o Departamento
        print("\nSeleccione una opción:")
        print("1. Carrera")
        print("2. Departamento")
        opcion = input("Ingrese el número correspondiente a su elección: ")

        # Validar la opción ingresada por el usuario
        while opcion not in ["1", "2"]:
            print("Opción no válida. Por favor, ingrese 1 para Carrera o 2 para Departamento.")
            opcion = input("\nIngrese el número correspondiente a su elección: ")

        # Asignar la carrera o departamento según la elección del usuario
        if opcion == "1":
            pass
            
        elif opcion == "2":
            departamento = input("Ingrese su nombre de departamento: ")
            while not departamento.isalpha() or len(departamento) == 0:
                print("Error!!! Dato Inválido.")
                departamento = input("\nIngrese su departamento: ")
                       
            
        list_seguidores = []#los seguidores de la misma carrera se siguen automaticamente
        
             
# ADMIN --------------------------------------------------------------------------------------------------
    def login_admin(self):

        while True:
            username = input("Ingrese su username: ")
            email = input("Ingrese su correo: ")
            # Validar credenciales
            if username == "Antonio_24" and email == "aguerra@correo.unimet.edu.ve":
                return True
            elif username == "Jose22" and email == "jose.filardi@correo.unimet.edu.ve":
                return True
            else:
                print("Credenciales inválidas.")
                print("Bienvenido al menú de administración.")
                print("\nOpciones:")
                print("\n1. Buscar usuarios")
                print("2. Eliminar un post") #Eliminar un post que considera ofensivo
                print("3. Eliminar un comentario ofensivo")
                print("4. Borrar la cuenta de un usuario")#Eliminar un comentario ofensivo
                print("5. Salir de la aplicacion")
                
                opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
                while not (opcion.isnumeric()) or (not int(opcion) in range(1,6)):
                    print("Error!!! Dato Inválido.")
                    opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                    
                if opcion == 1:
                filtro = input("Ingrese el filtro de búsqueda (username, carrera o departamento): ")
                tipo_usuario = input("Ingrese el tipo de usuario (estudiante o profesor): ")
                user_encontrados = App.buscar_user(self, filtro)
                if user_encontrados:
                    print("Usuarios encontrados:")
                    for usuario in user_encontrados:
                        print(f"Nombre: {usuario.nombre} {usuario.apellido}")
                        print(f"Username: {usuario.username}")
                        if isinstance(usuario, Estudiante):
                            print(f"Carrera: {usuario.carrera}")
                        else:
                            print(f"Departamento: {usuario.departamento}")
                        print("-----------------------")
                else:
                    print("No se encontraron usuarios con el filtro especificado.")
                    
    def buscar_user(self, filtro):
        usuarios_filtrados = []
        for usuario in self.list_user:
            if isinstance(usuario, Estudiante) and filtro == "carrera":
                if usuario.carrera == filtro:
                    usuarios_filtrados.append(usuario)
            elif isinstance(usuario, Profesor) and filtro == "departamento":
                if usuario.departamento == filtro:
                    usuarios_filtrados.append(usuario)
        else:
            return "El usuario buscado no existe"
        return usuarios_filtrados
    
    def is_email(email:str):               
        if "@" in email and email.count('@')==1:                            
                div=email.split('@')
                
                before_arroba=div[0]
                count_up = 0
                count_low = 0
                count_num = 0
                for i in before_arroba:
                    if i.isalpha() and i.isupper():
                      count_up += 1
                    if i.isalpha() and i.islower():
                      count_low += 1
                    if i.isnumeric():
                      count_num += 1
                if len(before_arroba)>6 and count_up != 0 and count_low != 0 and count_num != 0: #Al menos una mayuscula, una minuscula, un numero y len>4
                        val_before_arroba=True
                else:
                       val_before_arroba=False

                after_arroba=div[1]
                if 'gmail.com' in after_arroba or 'hotmail.com' in after_arroba: #dominios requeridos
                       val_after_arroba=True
                else:
                       val_after_arroba=False
                
                if val_before_arroba and val_after_arroba:
                       return True
                else:
                      return False
        else:
              return False