import requests
from validaciones import *
from Estudiante import Estudiante
from Profesor import Profesor
from Post import Post
from Multimedia import Multimedia
from Admin import Admin
class App:
    
    def __init__(self):
        self.list_post = []
        self.list_user = []
        self.list_estudiantes = []
        self.list_profesores = []
        self.list_carreras = []
        self.list_departamento = []
        self.list_admin = []
        self.list_admin.extend([
            Admin("aguerra@unimet.edu.ve","Antonio24"),
            Admin("jose.filardi@correo.unimet.edu.ve","Jose22")
        ])
        self.user_sesion = []

    #Cargar datos
    #####################################################################################################
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
            caption = []
            caption.append(dato2["caption"])
            fecha = dato2["date"]
            etiquetas = dato2["tags"]
            tipo_multimedia = dato2["multimedia"]["type"]
            url = dato2["multimedia"]["url"]
            like = 0

            multimedia = Multimedia(tipo_multimedia, url)
            post = Post(like, editor, tipo, caption, fecha, etiquetas, multimedia)

            self.list_post.append(post)
    ####################################################################################################
    
    #Menu de admin
    def menu_admin(self):  
        while True:
            print("\n")
            print(25*" " + "=" * 24)
            print(25*" " + "|~|    MENU ADMIN    |~|")
            print(25*" " + "=" * 24)
            print("\n")
            print(22*" " + "=" * 30)
            print(22*" " + "|1|    Eliminar un Post    |1|")
            print(22*" " + "=" * 30)
            print(" ")
            print(20*" " + "=" * 34)
            print(20*" " + "|2|   Eliminar un Comentario   |2|")
            print(20*" " + "=" * 34)
            print(" ")
            print(21*" " + "=" * 31)
            print(21*" " + "|3|   Eliminar un Usuario   |3|")
            print(21*" " + "=" * 31)
            print(" ")
            print("=" * 20)
            print("|4|     Salir    |4|")
            print("=" * 20)

            opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion.isnumeric()) or (not int(opcion) in range(1,5)):
                    print("Error!!! Dato Inválido.")
                    opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")        
            if opcion == "1":
                self.eliminar_post()
            elif opcion == "2":        
                self.eliminar_comentario()
            elif opcion == "3":
                self.eliminar_user()
            else:
                self.login()
    
    #Eliminar Post
    def eliminar_post(self):
        #Mostrar todos los post
        for i in range(0,len(self.list_post)):
            print(f"{i+1}. {self.list_post[i].show_post()}")
        
        #Seleccionar post
        option = input("Ingrese el numero del post que desea eliminar: ")
        while (not option.isnumeric()) or (not int(option) in range(1,len(self.list_post))):
            print("Error!!! Dato Inválido.")
            option = input("Ingrese el numero del post que desea eliminar: ")

        #Indice del post que se desea eliminar
        index = int(option) - 1

        #Eliminar post de la lista segun el indice
        self.list_post.pop(index)

        print("Post eliminado con exito.")
    
    #Eliminar comentario de un post
    def eliminar_comentario(self):
        #Mostrar todos los post
        for i in range(0,len(self.list_post)):
            print(f"{i+1}. {self.list_post[i].show_post()}")
        
        #Seleccionar post
        option = input("Ingrese el numero del post que desea eliminar: ")
        while (not option.isnumeric()) or (not int(option) in range(1,len(self.list_post))):
            print("Error!!! Dato Inválido.")
            option = input("Ingrese el numero del post que desea eliminar: ")
        
        index = int(option) - 1

        #Guardar en una variable el post relacionado con el comentario que se desea elminar
        post = self.list_post[index]

        #Mostrar los comentarios del post seleccionado
        for i in range(len(post.caption)):
            print(f"{i+1}. {post.caption[i]}")

        #Elegir el comentario del post seleccionado que dessea eliminar
        option = input("Ingrese el numero del comentario que desea eliminar: ")
        while (not option.isnumeric()) or (not int(option) in range(len(post.caption))):
            print("Error!!! Dato Inválido.")
            option = input("Ingrese el numero del comentario que desea eliminar: ")
        
        #Indice del comentario a eliminar
        index_caption = int(option) - 1

        #Eliminar el comentario por el indice
        post.caption.pop(index_caption)

        print("Comentario eliminado con exito")
        
    def eliminar_user(self):
        #Mostrar los usuarios registrados
        for i in range(0,len(self.list_user)):
            if self.list_user[i].tipo == "Estudiante":
                print(f"{i+1}. {self.list_post[i].show_student()}")
            else:
                print(f"{i+1}. {self.list_post[i].show_teacher()}")
        
        #Elegir el numero relacionado al usuario que se desea eliminar
        option = input("Ingrese el numero del usuario que desea eliminar: ")
        while (not option.isnumeric()) or (not int(option) in range(len(self.list_user))):
            print("Error!!! Dato Inválido.")
            option = input("Ingrese el numero del usuario que desea eliminar: ")
        
        index = int(option) - 1

        if self.list_user[index].tipo == "Estudiante":
            #Eliminar el estudiante de la lista de estudiantes
            for i in range(len(self.list_estudiantes)):
                if self.list_user[index].username == self.list_estudiantes[i].username:
                    self.list_estudiantes.pop(i)
                    break
        else:
            #Eliminar el profesor de la lista de profesores
            for i in range(len(self.list_profesores)):
                if self.list_user[index].username == self.list_profesores[i].username:
                    self.list_profesores.pop(i)
                    break
        
        #Por ultimo, elimino al usuario de la lista de usuario
        self.list_user.pop(index)
        print("Usuario eliminado")

    def menu_user(self):
        while True:
            print("\n")
            print(26*" " + "=" * 18)
            print(26*" " + "|~|    MENU    |~|")
            print(26*" " + "=" * 18)
            print("\n")
            print(20*" " + "=" * 30)
            print(20*" " + "|1|        Perfil      |1|")
            print(20*" " + "=" * 30)
            print(" ")
            print(22*" " + "=" * 26)
            print(22*" " + "|2|     Multimedia     |2|") 
            print(22*" " + "=" * 26)
            print(" ")
            print(22*" " + "=" * 26)
            print(22*" " + "|3|     Interaccion     |3|") 
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
        while True:
            print("\n")
            print(24*" " + "=" * 26)
            print(24*" " + "|~|    MENU  PERFIL    |~|")
            print(24*" " + "=" * 26)
            print("\n")
            print(27*" " + "=" * 19)
            print(27*" " + "|1|    Datos    |1|")
            print(27*" " + "=" * 19) 
            print(" ")
            print(22*" " + "=" * 29)
            print(22*" " + "|2|     Editar Perfil     |2|") 
            print(22*" " + "=" * 29)
            print(" ")
            print(22*" " + "=" * 29)
            print(22*" " + "|3|     Borrar Cuenta     |3|") 
            print(22*" " + "=" * 29) 
            print(" ")
            print(22*" " + "=" * 29)
            print(22*" " + "|4|    Volver al MENU     |4|")
            print(22*" " + "=" * 29)

            
            opcion_perfil = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not opcion_perfil.isnumeric()) or (not int(opcion_perfil) in range(1,5)):
                        print("Error!!! Dato Inválido.")
                        opcion_perfil = input("Ingrese el número correspondiente a la acción que desea realizar: ")
            
            if opcion_perfil == "1":
                self.datos_perfil()
            elif opcion_perfil == "2":
                self.modificar_perfil()
            elif opcion_perfil == "3":
                self.borrar_cuenta()
            else:
                self.menu_user()
 
    def datos_perfil(self):
        if self.user_sesion[0].tipo == "Profesor":
            self.user_sesion[0].show_teacher()
        else:
            self.user_sesion[0].show_student()

    def borrar_cuenta(self):
        print("Y: yes, N: no")
        option = input("Desea borrar su cuenta: ").upper()

        if option == "Y":
            #Eliminar de las sublistas depende del tipo

            if self.user_sesion[0].tipo == "Estudiante":
                #Eliminar de la lista de estudiantes
                for i in range(len(self.list_estudiantes)):
                    if self.list_estudiantes[i].username == self.user_sesion[0].username:
                        self.list_estudiantes.pop(i)
                        break
            else:
                #Eliminar de la lista de profesores
                for i in range(len(self.list_profesores)):
                    if self.list_profesores[i].username == self.user_sesion[0].username:
                        self.list_profesores.pop(i)
                        break
            #Por utlimo, elimnar de la lista general de usuarios
            for i in range(len(self.list_user)):
                if self.list_user[i].username == self.user_sesion[0].username:
                    self.list_user.pop(i)
                    break
            self.user_sesion.pop(0)
            print("Cuenta Eliminada.\n")
            self.login()
    

    #Funcion para modificar el perfil
    def  modificar_perfil(self):
        print(27*" " + "=" * 19)
        print(27*" " + "|*|    Datos    |*|")
        print(27*" " + "=" * 19)
        print(f"Nombre: {self.user_sesion[0].firstname}")
        print(f"Apellido: {self.user_sesion[0].lastname}")
        print(f"Email: {self.user_sesion[0].username}")
        print(f"Username: {self.user_sesion[0].email}")
        
        while True:
            print("\nOpciones de Modificacion:")
            print("1. Modificar Nombre")
            print("2. Modificar Apellido")
            print("3. Modificar UserName")
            print("4. Modificar Email")

            option = input("Ingrese una opcion: ")
            while (not option.isnumeric()) or (not int(option) in range(1,4)):
                print("Error!!! Dato Inválido.")
                option = input("Ingrese una opcion: ")
            
            if option == "1":
                nombre = input("Ingrese el nuevo nombre: ")
                validar_letras(nombre)
                self.user_sesion[0].firstname = nombre

            elif option == "2":
                apellido = input("Ingrese el nuevo apellido: ")
                validar_letras(apellido)
                self.user_sesion[0].lastname = apellido
            elif option == "3":
                username = input("Ingrese el nuevo username: ")
                validar_username_unique(username, self.list_user)
                self.user_sesion[0].username = username
            elif option == "4":
                email = input("Ingrese el nuevo email: ")
                validar_email_unique(email, self.list_user)
                self.user_sesion[0].email = email
            else:
                break                


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