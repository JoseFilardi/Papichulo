from App import App

def main():
    app = App()
    
    #Cargar Datos
    app.api_perfil()
    app.api_post()
    app.llenado_carreras()
    app.llenado_department()

    app.login()

main()