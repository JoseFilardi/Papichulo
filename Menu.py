def login():
    
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
            pass
            #self.inicio
        elif opcion == "2":
            pass
            #self.registrar_user
        else:
            print("\n")
            print("=" * 20)
            print("|*|    ADIOS!!   |*|")
            print("|*|   NOS VEMOS  |*|")
            print("=" * 20)  
            break

       
def buscador():
    
    while True:
        print("\n")
        print(24*" " + "=" * 22)
        print(24*" " + "|~|    BUSCADOR    |~|") 
        print(24*" " + "=" * 22)
        print("\n")
        print(22*" " + "=" * 26)
        print(22*" " + "|1|     Buscar Post    |1|")
        print(22*" " + "=" * 26)
        print(" ")
        print(20*" " + "=" * 30)
        print(20*" " + "|2|   Buscar Comentario    |2|")
        print(20*" " + "=" * 30)
        print(" ")
        print(21*" " + "=" * 28)
        print(21*" " + "|3|    Buscar Usuario    |3|") # Buscar perfiles en función de los siguientes filtros:a. Usernameb. Carrera o departamento
        print(21*" " + "=" * 28) # Mostrar: a. Nombre y username b. Listado de publicaciones c. Es posible acceder a una publicación desde el listado del perfil
        print(" ")
        print("=" * 20)
        print("|4|     Salir    |4|")
        print("=" * 20)
        opcion = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
        while (not opcion.isnumeric()) or (not int(opcion) in range(1,5)):
                    print("Error!!! Dato Inválido.")
                    opcion = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if opcion == "1":
            pass #self.buscar_post()
        elif opcion == "2":        
            pass #self.buscar_comen()
        elif opcion == "3":
            pass #self.buscar_user()
        elif opcion == "4":
            admin()
   

    
def menu_user():
    
    
    print("\n")
    print(25*" " + "=" * 20)
    print(25*" " + "|~|    PERFIL    |~|")
    print(25*" " + "=" * 20)
    print("\n")
    print(20*" " + "=" * 30)
    print(20*" " + "|1|    Datos del Perfil    |1|") # Editra  Mi Perfil # Cambiar la información personal de la cuenta. Borrar los datos de la cuenta.
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
        pass #self.perfil()
    elif opcion == "2":
        pass #self.multimedia()
    elif opcion == "3":        
        pass #self.interaccion()
    elif opcion == "4":
        login()
        

        
          
def admin():
    
    while True:
        print("\n")
        print(25*" " + "=" * 24)
        print(25*" " + "|~|    MENU ADMIN    |~|")
        print(25*" " + "=" * 24)
        print("\n")
        print(26*" " + "=" * 22)
        print(26*" " + "|1|     Buscar     |1|") # Buscar perfiles en función de los siguientes filtros:a. Usernameb. Carrera o departamento
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
            buscador()
        elif opcion == "2":
            pass #self.eliminar_post()
        elif opcion == "3":        
            pass #self.eliminar_comen()
        elif opcion == "4":
            pass #self.eliminar_user()
        elif opcion == "5":
            login()

def perfil():
    pass

def multimedia():
    pass

def interaccion():
    pass
