from User import User

class Profesor(User):
    def __init__(self, id, firstName, apellido, username, email, departamento):
        super().__init__(id, firstName, apellido, username, email)
        self.departamento = departamento