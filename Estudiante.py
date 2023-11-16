from User import User

class Estudiante(User):
    
    def __init__(self, id, firstName, apellido, username, email, carrera):
        super().__init__(id, firstName, apellido, username, email)
        self.carrera = carrera