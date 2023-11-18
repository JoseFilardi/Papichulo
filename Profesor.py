from User import User

class Profesor(User):
    def __init__(self, id, firstname, lastname, username, email, departamento, seguidores, tipo):
        self.departamento = departamento
        super().__init__(id, firstname, lastname, username, email, seguidores, tipo)

    def show_teacher(self):
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Departamento: {self.departamento}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)