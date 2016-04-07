from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from ConeccionDB import insertar, consultarlogin


class ScreenManagement(ScreenManager):
    pass


class Intro(Screen):
    username_b = ObjectProperty()
    password_b = ObjectProperty()

    def login(self):
        cerd = (self.username_b.text)
        passw = (self.password_b.text)
        consultarlogin(cerd, passw)


class Registro(Screen):
    nombre_b = ObjectProperty()
    apellido_b = ObjectProperty()
    nacimiento_b = ObjectProperty()
    cedula_b = ObjectProperty()
    carrera_b = ObjectProperty()

    def regis(self):
        nombre = (self.nombre_b.text)
        apellido = (self.apellido_b.text)
        nacimiento = (self.nacimiento_b.text)
        cedula  = (self.cedula_b.text)
        carrera = (self.carrera_b.text)
        insertar(cedula, nombre, carrera, apellido, nacimiento)


class Menu(Screen):
    pass


class Materias(Screen):
    pass


class Calendario(Screen):
    pass


class Perfil(Screen):
    pass


class Eventos(Screen):
    pass


kivyfile = Builder.load_file("Interfaz.kv")


class Plataforma(App):
    def build(self):
        return kivyfile


if __name__ == "__main__":
    try:
        Plataforma().run()
    except Exception as e:
        print("Error: ", e)
