class Multimedia:
    
    def __init__(self, tipo, url):
        self.tipo = tipo
        self.url = url
    
    def show_multimedia(self):
        print(f"""
        Tipo: {self.tipo}, Url: {self.url}
    """)