import requests
from Estudiante import Estudiante
from Profesor import Profesor
from Post import Post
from Multimedia import Multimedia
class App:
    
    def __init__(self):
        self.list_post = []
        self.list_user = []
        self.list_estudiantes = []
        self.list_profesores = []
        self.list_carreras = []
        self.list_departamento = []
        self.list_admin = []

    def api_perfil(self):
        link="https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json"
        responce = requests.get(link)
        datos = responce.json()
        
        for dato in datos:
           id = dato["id"]
           firstname = dato["firstName"]
           lastname = dato["lastName"]
           email = dato["email"]
           username = dato["username"]
           following = dato["following"]

           if dato["type"] == "professor":
               tipo = dato["type"]
               departamento = dato["department"]
               teacher = Profesor(id,firstname, lastname, username, email, departamento, following, tipo)
               self.list_profesores.append(teacher)
               self.list_user.append(teacher)
           else:
               tipo = dato["type"]
               carrera = dato["major"]
               student = Estudiante(id, firstname, lastname, username, email, carrera, following, tipo)
               self.list_estudiantes.append(student)
               self.list_user.append(student)

        #for user in self.list_user:
        #    if type(user) == Profesor:
        #       user.show_teacher()
    
    def api_post(self):
        link = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json"
        responce = requests.get(link)
        datos2 = responce.json()

        for dato2 in datos2:
            editor = dato2["publisher"]
            tipo = dato2["type"]
            caption = dato2["caption"]
            fecha = dato2["date"]
            etiquetas = dato2["tags"]
            tipo_multimedia = dato2["multimedia"]["type"]
            url = dato2["multimedia"]["url"]
            like = 0

            multimedia = Multimedia(tipo_multimedia, url)
            post = Post(like, editor, tipo, caption, fecha, etiquetas, multimedia)

            self.list_post.append(post)

    def menu_user(self):
        print("Hola usuario")
    
    def menu_admin(self):
        pass

    def inicio_sesion(self):
        while True:
            email = input("Ingrese su correo: ")
            username = input("Ingrese su username: ")
            
            for user in self.list_user:
                if user.email == email:
                    if user.username == username:
                        self.menu_user()
                        break
            
            for admin in self.list_admin:
                if admin.email == email:
                    if admin.user == username:
                        self.menu_user()

            print("Error en el email o en el username, por favor verifique")  
    

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

        #Corregir validacion del correo, por favor quitar el while true wtf
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

        # Corregir de aqui para abajo por favor, es un chiste JAJAJAJAJAJAJAJAJA

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

    
    def login(self):
        self.api_perfil()
        self.api_post()
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
                self.inicio_sesion()
            elif opcion == "2":
                self.registrar_user()
            elif opcion == "3":
                break
