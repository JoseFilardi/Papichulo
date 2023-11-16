class Post:
    
    def __init__(self, likes, comentario, ):
        self.likes = likes
        self.comentario = comentario
        
    def show_post(self):
        return f"""
    Likes: {self.likes}
    Comentario: {self.comentario}    
    """
    #def show_comentario(self):
    #    return f"""
    #Usuario: {self.user}
    #Post: {self.post} 
    #Comentario: {self.comentario}
    #Fecha: {self.fecha}
    #"""