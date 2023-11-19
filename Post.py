class Post:
    
    def __init__(self, likes, editor, tipo, caption, fecha, etiquetas, multimedia):
        self.likes = []
        self.editor = editor
        self.tipo = tipo 
        self.caption = []
        self.fecha = fecha
        self.etiquetas = etiquetas
        self.multimedia = multimedia
        
    def show_post(self):
        print( f"""
    Likes: {len(self.likes)}   
    Editor: {self.editor}
    Tipo: {self.tipo}
    Fecha: {self.fecha}
    Etiquetas:
    """)
        for etiqueta in self.etiquetas:
            print(etiqueta)
        print("Caption: ")
        
        for caption in self.caption:
            print(caption)
        print(f"Multimedia: {self.multimedia.show_multimedia()}")
            
