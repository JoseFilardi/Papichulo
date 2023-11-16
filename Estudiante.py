from User import User

class Estudiante(User):
    
    def __init__(self, id, firstname, lastname, username, email, carrera, seguidores, tipo):
        self.carrera = carrera
        self.tipo = "Estudiante"
        super().__init__(id, firstname, lastname, username, email, seguidores, tipo)

    def show_student(self):
        print(f"""
            Nombre: {self.firstname}
            Apellido: {self.lastname} 
            Nombre de usuario: {self.username}
            email: {self.email}
            Tipo: {self.tipo}
            Carrera: {self.carrera}
            Seguidores:
        """)
        for id in self.seguidores:
            print(id)