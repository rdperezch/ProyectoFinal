from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from ConeccionDB import insertar, consultarlogin, conect, consultarperfil, perfil


class ScreenManagement(ScreenManager):
    pass


class Intro(Screen):
    username_b = ObjectProperty()
    password_b = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/Campus_UIP.jpg'))

    def login(self):
        stat = self.ids.stats
        try:
            cerd = self.username_b.text
            passw = self.password_b.text
            consultarlogin(cerd, passw)
            logic = conect()
            if logic:
                print("conecto")
                stat.color = (0, 1, 0, 1)
                stat.text = "Conecto"
                self.manager.current = 'menu'
                global manejador
                manejador = cerd
            if not logic:
                stat.color = (1, 0, 0, 1)
                stat.text = "Fallo"
                print("no conecto")
        except Exception as e:
            stat.color = (1, 0, 0, 1)
            stat.text = "Sin coneccion a internet"
            print("Error en Login: sin coneccion", e)

    def resetForm(self):
        self.ids['username_i'].text = ""
        self.ids['password_i'].text = ""

    def resetLog(self):
        self.ids['stats'].text = ""


class Registro(Screen):
    cedula_b = ObjectProperty()
    nombre_b = ObjectProperty()
    seg_nombre_b = ObjectProperty()
    apellido_b = ObjectProperty()
    seg_apellido_b = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/blueback.png'))

    def regis(self):
        nombre = self.nombre_b.text
        apellido = self.apellido_b.text
        seg_nombre = self.seg_nombre_b.text
        cedula = self.cedula_b.text
        seg_apellido = self.seg_apellido_b.text
        insertar(cedula, nombre, seg_nombre, apellido, seg_apellido)


class Registro2(Screen):
    pass


class Menu(Screen):
    manejador2 = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/Build.jpg'))

    def login(self):
        stat = self.ids.log
        stat.color = (0, 0, 1, 1)
        stat.text = "Loggin as " + manejador

    def logout(self):
        self.manager.get_screen('intro').resetLog()
        self.manager.get_screen('intro').resetForm()


class Materias(Screen):
    grid = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/backazul.png'))


class Calendario(Screen):
    background_image = ObjectProperty(Image(source='data/backazul.png'))


class Perfil(Screen):
    grid = ObjectProperty()
    background_image = ObjectProperty(Image(source='data/backazul.png'))

    def consultar(self):
        cedula = manejador
        consultarperfil(cedula)
        print(perfil())
        datos = perfil()
        for x in datos:
            print(x)
            self.grid.add_widget(Label(text=str(x), font_size=10))
        for x in datos:
            print(datos.get(x))
            self.grid.add_widget(Label(text=str(datos.get(x)), font_size=10))

    def Borrar(self):
        self.grid.clear_widgets()


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
