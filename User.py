class User:
    def __init__(self, id, firstname, lastname, username, email, seguidores, tipo):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.seguidores = seguidores
        self.tipo = tipo

    def show_user(self):
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)