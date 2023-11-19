#ADMIN  

#BUSCADOR
def buscar_post():
    pass
def buscar_comen():
    pass
def buscar_user():
    pass


#MENU USER 
def multimedia():
    pass
def interaccion():
    pass

#MULTIMEDIA // PARETE DEL MENU USER
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
def buscar_post():
    pass  #Buscar posts en función de los siguientes filtros:a. User / b. Hashtags (#)
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
  
#INRERACCION // PARETE DEL MENU USER
def seguir_usuario():
    pass
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