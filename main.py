from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from ConeccionDB import insertar, consultarlogin


class ScreenManagement(ScreenManager):
    pass


class Intro(Screen):
    username_b = ObjectProperty()
    password_b = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/Campus_UIP.jpg'))

    def login(self):
        cerd = (self.username_b.text)
        passw = (self.password_b.text)
        # consultarlogin(cerd, passw)


class Registro(Screen):
    nombre_b = ObjectProperty()
    apellido_b = ObjectProperty()
    seg_nombre_b = ObjectProperty()
    cedula_b = ObjectProperty()
    seg_apellido_b = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/blueback.png'))

    def regis(self):
        nombre = (self.nombre_b.text)
        apellido = (self.apellido_b.text)
        seg_nombre = (self.seg_nombre_b.text)
        cedula = (self.cedula_b.text)
        seg_apellido = (self.seg_apellido_b.text)
        # insertar(cedula, nombre, seg_nombre, apellido, seg_apellido)


class Menu(Screen):
    background_image = ObjectProperty(Image(source='data/Build.jpg'))


class Materias(Screen):
    grid = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/backazul.png'))


class Calendario(Screen):
    background_image = ObjectProperty(Image(source='data/backazul.png'))


class Perfil(Screen):
    background_image = ObjectProperty(Image(source='data/backazul.png'))


class Eventos(Screen):
    background_image = ObjectProperty(Image(source='data/backazul.png'))

kivyfile = Builder.load_file("Interfaz.kv")


class Plataforma(App):
    def build(self):
        return kivyfile


if __name__ == "__main__":
    try:
        Plataforma().run()
    except Exception as e:
        print("Error: ", e)