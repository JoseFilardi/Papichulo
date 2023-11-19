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
   
def buscar_post(): #Buscar posts en función de los siguientes filtros:a. User / b. Hashtags (#)
    pass
def buscar_comen():
    pass
def buscar_user(): # Buscar perfiles en función de los siguientes filtros:a. Usernameb. Carrera o departamento
    pass       # Mostrar: a. Nombre y username b. Listado de publicaciones c. Es posible acceder a una publicación desde el listado del perfil


def multimedia():
    while True:
        print("\n")
        print(21*" " + "=" * 31)
        print(21*" " + "|~|     MENU  MULTIMEDIA    |~|")
        print(21*" " + "=" * 31)
        print("\n")
        print(22*" " + "=" * 29)
        print(22*" " + "|1|     Registrar POST    |1|")
        print(22*" " + "=" * 29) 
        print(" ")
        print(23*" " + "=" * 27)
        print(23*" " + "|2|     Buscar POSTS    |2|") 
        print(23*" " + "=" * 27)
        print(" ")
        print(24*" " + "=" * 25)
        print(24*" " + "|3|     Ver POST     |3|") 
        print(24*" " + "=" * 25) 
        print(" ")
        print(22*" " + "=" * 29)
        print(22*" " + "|4|    Volver al MENU     |4|")
        print(22*" " + "=" * 29)

        
        opcion_muilti = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
        while (not opcion_muilti.isnumeric()) or (not int(opcion_muilti) in range(1,5)):
                    print("Error!!! Dato Inválido.")
                    opcion_muilti = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if opcion_muilti == "1":
            pass #registrar_post():
        elif opcion_muilti == "2":
            pass #buscar_post()
        elif opcion_muilti == "3":
            pass #ver_post(): 
        elif opcion_muilti == "4":
            pass #menu_user()

def registrar_post(username):
    print("\n")
    print(22*" " + "=" * 29)
    print(22*" " + "|*|     Registrar POST    |*|")
    print(22*" " + "=" * 29) 
    print(" ")
    multimedia = input("Ingrese la URL de la multimedia (foto o video): ")
    descripcion = input("Ingrese la descripción del post: ")
    hashtags = input("Ingrese los hashtags del post (separados por espacio): ").split()
    fecha_publicacion = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")

    # Agregar el nuevo post a la lista de posts
    nuevo_post = {
        'username': username,
        'multimedia': multimedia,
        'descripcion': descripcion,
        'hashtags': hashtags,
        'fecha_publicacion': fecha_publicacion,
        'likes': 0,
        'comentarios': []
    }
    #posts.append(nuevo_post)

    print("=" * 39)
    print("|*|   ¡Post registrado con exito!   |*|")
    print("=" * 39)         
#def buscar_post(): #Buscar posts en función de los siguientes filtros:a. User / b. Hashtags (#)
def ver_post(username, post):
    print("\n--- Ver Post ---")
    print(f"\nUsername: {post['username']}")
    print(f"Multimedia: {post['multimedia']}")
    print(f"Descripción: {post['descripcion']}")
    print(f"Hashtags: {', '.join(post['hashtags'])}")
    print(f"Fecha de Publicación: {post['fecha_publicacion']}")
    print(f"Likes: {post['likes']}")
    print("Comentarios:")
    for comentario in post['comentarios']:
        print(f"- {comentario['usuario']}: {comentario['comentario']}")

    

def interaccion():
    
    while True:
        print("\n")
        print(21*" " + "=" * 32)
        print(21*" " + "|~|    MENU  INTERACCION     |~|")
        print(21*" " + "=" * 32)
        print("\n")
        print(22*" " + "=" * 30)
        print(22*" " + "|1|    Seguir a Usuario    |1|")
        print(22*" " + "=" * 30) 
        print(" ")
        print(18*" " + "=" * 37)
        print(18*" " + "|2|   Dejar de seguir a Usuario   |2|") 
        print(18*" " + "=" * 37)
        print(" ")
        print(22*" " + "=" * 29)
        print(22*" " + "|3|     Comentar POST     |3|") 
        print(22*" " + "=" * 29) 
        print(" ")
        print(19*" " + "=" * 34)
        print(19*" " + "|4|     Dar Like a un POST     |4|") 
        print(19*" " + "=" * 34)
        print(" ")
        print(13*" " + "=" * 46)
        print(13*" " + "|5|     Eliminar comentario de un POST     |5|") 
        print(13*" " + "=" * 46)
        print(" ")
        print(21*" " + "=" * 29)
        print(21*" " + "|6|    Volver al MENU     |6|")
        print(21*" " + "=" * 29) 
        
        opcion_inte = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
        while (not opcion_inte.isnumeric()) or (not int(opcion_inte) in range(1,7)):
                    print("Error!!! Dato Inválido.")
                    opcion_inte = input("Ingrese el número correspondiente a la acción que desea realizar: ")

        if opcion_inte == "1":
            pass #seguir_usuario():
        elif opcion_inte == "2":
            pass #dejar_de_seguir():
        elif opcion_inte == "3":
            pass #comentar_post():
        elif opcion_inte == "4":
            pass #dar_like():
        elif opcion_inte == "5":
            pass #eliminar_comentario_ofensivo():
        elif opcion_inte == "6":
            pass #menu_user()

def seguir_usuario():
    pass#Cuando un usuario accede a la cuenta de otro usuario, se deberá mostrar la siguiente información:
    #a. Nombre y username
    #b. Listado de publicaciones
    #c. Es posible acceder a una publicación desde el listado del perfil   
def dejar_de_seguir():
    pass
def comentar_post(usuario, post):
    print("\n")
    print(22*" " + "=" * 29)
    print(22*" " + "|*|     Comentar POST     |*|") 
    print(22*" " + "=" * 29) 
    comentario = input("Ingrese su comentario: ")
    fecha_publicacion = '2023-01-04'  # Obtener la fecha actual o de alguna otra manera

    # Agregar el comentario al post
    post['comentarios'].append({
        'username': usuario['username'],
        'comentario': comentario,
        'fecha_publicacion': fecha_publicacion
    })

    print("=" * 33)
    print("|*|   ¡Comentario agregado!   |*|")
    print("=" * 33) 
def dar_like():
    pass
def eliminar_comentario_ofensivo():
    pass


