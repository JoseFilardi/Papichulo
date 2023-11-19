import requests
from validaciones import *
from Estudiante import Estudiante
from Profesor import Profesor
from Post import Post
from Multimedia import Multimedia
import Menu
class App:
    
    def __init__(self):
        self.list_post = []
        self.list_user = []
        self.list_estudiantes = []
        self.list_profesores = []
        self.list_carreras = []
        self.list_departamento = []
        self.list_admin = []
        self.user_sesion = []

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
        
    def llenado_carreras(self):
        for estudiante in self.list_estudiantes:
            if estudiante.carrera not in self.list_carreras:
                self.list_carreras.append(estudiante.carrera)
    
    def llenado_department(self):
        for profesor in self.list_profesores:
            if profesor.departamento not in self.list_departamento:
                self.list_departamento.append(profesor.departamento)
    
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

    def menu_admin(self):  
        while True:
            print("\n")
            print(25*" " + "=" * 24)
            print(25*" " + "|~|    MENU ADMIN    |~|")
            print(25*" " + "=" * 24)
            print("\n")
            print(26*" " + "=" * 22)
            print(26*" " + "|1|     Buscar     |1|") 
            print(26*" " + "=" * 22)
            print("")
            print(22*" " + "=" * 30)
            print(22*" " + "|2|    Eliminar un Post    |2|")
            print(22*" " + "=" * 30)
            print(" ")
            print(20*" " + "=" * 34)
            print(20*" " + "|3|   Eliminar un Comentario   |3|")
            print(20*" " + "=" * 34)
            print(" ")
            print(21*" " + "=" * 31)
            print(21*" " + "|4|   Eliminar un Usuario   |4|")
            print(21*" " + "=" * 31)
            print(" ")
            print("=" * 20)
            print("|5|     Salir    |5|")
            print("=" * 20)

            opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion.isnumeric()) or (not int(opcion) in range(1,6)):
                    print("Error!!! Dato Inválido.")
                    opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")        
            if opcion == "1":
                #buscador()
                pass
            elif opcion == "2":
                pass #self.eliminar_post()
            elif opcion == "3":        
                pass #self.eliminar_comen()
            elif opcion == "4":
                pass #self.eliminar_user()
            else:
                #login()
                pass
    
    def menu_user(self):

        while True:
            print("\n")
            print(26*" " + "=" * 18)
            print(26*" " + "|~|    MENU    |~|")
            print(26*" " + "=" * 18)
            print("\n")
            print(20*" " + "=" * 30)
            print(20*" " + "|1|    Datos del Perfil    |1|") #self.perfil()
            print(20*" " + "=" * 30)
            print(" ")
            print(22*" " + "=" * 26)
            print(22*" " + "|2|     Multimedia     |2|") 
            print(22*" " + "=" * 26)
            print(" ")
            print(22*" " + "=" * 26)
            print(22*" " + "|3|     Interaccion     ||") 
            print(22*" " + "=" * 26) 
            print(" ")
            print("=" * 20)
            print("|4|     Salir    |4|")
            print("=" * 20)

            opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion.isnumeric()) or (not int(opcion) in range(1,5)):
                        print("Error!!! Dato Inválido.")
                        opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")

            if opcion == "1":
                self.perfil()
            elif opcion == "2":
                pass #self.multimedia()
            elif opcion == "3":        
                pass #self.interaccion()
            else:
                self.user_sesion = []
                self.login()

    def perfil(self):
        if self.user_sesion[0].tipo == "Profesor":
            self.user_sesion[0].show_teacher()
        else:
            self.user_sesion[0].show_student()
        
        #Mostrar en ambos casos la opcion de modificar datos y una opcion para salir, esa salida dirigira al usuario al menu_user

        
    
    def inicio_sesion(self):
        while True:
            email = input("Ingrese su correo: ")
            username = input("Ingrese su username: ")  

            for user in self.list_user:
                if user.email == email:
                    if user.username == username:
                        self.user_sesion.append(user)
                        self.menu_user()
                        break
            
            for admin in self.list_admin:
                if admin.email == email:
                    if admin.username == username:
                        self.user_sesion.append(admin)
                        self.menu_admin()
                        break

            print("Error en el email o en el username, por favor verifique")
    
    def registrar_user(self):
        
        # Pedir información al usuario
        nombre = input("\nIngrese su nombre: ")
        validar_letras(nombre)

        apellido = input("Ingrese su apellido: ")
        validar_letras(apellido)

        #Probar la Validacion
        email = input("Ingrese su correo: ")
        while validar_email(email) != 1:
            email = input("Ingrese su correo: ")

        username = input("Ingrese su nombre de usuario: ")

        cedula = input("Ingrese su cedula: ")
        while (not cedula.isnumeric()) or (len(cedula) < 5):
            print("Opción no válida.")
            cedula = input("Ingrese su cedula: ")

        while validar_values_unique(email, username, id, self.list_user) == False:
            print("El email, la cedula o el username ya esta registrado")
            email = input("Ingrese su correo: ")
            while validar_email(email) != 1:
                email = input("Ingrese su correo: ")
            username = input("Ingrese su nombre de usuario: ")
            cedula = input("Ingrese su cedula: ")
            while (not cedula.isnumeric()) or (len(cedula) < 5):
                print("Opción no válida.")
                cedula = input("Ingrese su cedula: ")

        # Mostrar opciones para Estudiante o profesor
        print("\nSeleccione una opción:")
        print("1. Estudiante")
        print("2. Profesor")

        opcion = input("Ingrese el número correspondiente a su elección: ")
        while (not opcion.isnumeric()) or (not int(opcion) in range(1, 3)):
            print("Opción no válida.")
            opcion = input("\nIngrese la opcion: ")

        # Asignar la carrera o departamento según la elección del usuario
        if opcion == "1":
            for i in range(len(self.list_carreras)):
                print(f"{i}. {self.list_carreras[i]}")
        
            carrera = input("Ingrese el numero que corresponde a la carrera a la cual perteneces: ")
            while (not carrera.isnumeric()) or (not int(carrera) in range(0, len(self.list_carreras))):
                print("Opción no válida.")
                carrera = input("Ingrese el numero que corresponde a la carrera a la cual perteneces: ")
            
            major = self.list_carreras[int(carrera)]
            list_seguidores = []

            for estudiante in self.list_estudiantes:
                if estudiante.carrera == major:
                    list_seguidores.append(estudiante.id)

            estudiante = Estudiante(cedula, nombre, apellido,username, email, major, list_seguidores, tipo="Estudiante")
            estudiante.show_student()

            self.list_estudiantes.append(estudiante)
            self.list_user.append(estudiante)
            
            for user in self.list_user:
                user.show_user()

        else:

            for i in range(len(self.list_departamento)):
                print(f"{i}. {self.list_departamento[i]}")
            
            departamento = input("Ingrese su nombre de departamento: ")
            while (not departamento.isnumeric()) or (not int(departamento) in range(0, len(self.list_departamento))):
                print("Opción no válida.")
                departamento = input("\nIngrese su departamento: ")

            departament = self.list_departamento[int(departamento)]
            list_seguidores = []

            for profesor in self.list_profesores:
                if profesor.departamento == departament:
                    list_seguidores.append(profesor.id)
            
            profesor = Profesor(cedula, nombre, apellido, username, email, departament, list_seguidores,tipo="Profesor")

            self.list_profesores.append(profesor)
            self.list_user.append(profesor)
        
        print("Usuario creado con exito.") 
    
    
    def login(self):
        #Llenar datos iniciales a partir de la API
        while True:
            print("\n")
            print(23*" " + "=" * 27)
            print(23*" " + "|~|  M E T R O G R A M  |~|")
            print(23*" " + "=" * 27)
            print("\n")    
            print(20*" " + "=" * 33)
            print(20*" " + "|1|      Inicio de Sesión     |1|")
            print(20*" " + "=" * 33)
            print(" ")
            print(22*" " + "=" * 29)
            print(22*" " + "|2|        Registro       |2|")
            print(22*" " + "=" * 29)
            print(" ")
            print("=" * 20)
            print("|3|     Salir    |3|")
            print("=" * 20)   

            opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion.isnumeric()) or (not int(opcion) in range(1,4)):
                print("Error!!! Dato Inválido.")
                opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            if opcion == "1":
                self.inicio_sesion()

            elif opcion == "2":
                self.registrar_user()
            else:
                print("\n")
                print("=" * 20)
                print("|*|    ADIOS!!   |*|")
                print("|*|   NOS VEMOS  |*|")
                print("=" * 20)  
                break