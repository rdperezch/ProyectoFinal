from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy.uix.button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import calendar
import time

now = int(time.strftime("%d"))
mes = int (time.strftime("%m"))
anno = int(time.strftime("%Y"))

def ColocarEvento(day, month, year):
    if anno == year:
        #este sera mi diccionario donde vamos a tener nuestros eventos
        agenda = {'April':[5,20,30],'May':[9],'June':[13,25,30] }
        for listames in agenda:
             for listadia in agenda[listames]:
                 if listames==month and listadia == day:
                    return True
        else:
            status = False
        return status


class Calendar(Popup):
    day = NumericProperty(7)
    month = NumericProperty(12)
    year = NumericProperty(2016)
    root = BoxLayout(orientation = "vertical")

    def __init__(self, **kwargs):

        super(Popup, self).__init__(**kwargs)
        # Vamos a añadir un widget a este diseño
        self.add_widget(self.root)
        self.create_calendar()

    def create_calendar(self):
        self.day_str = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]
        self.month_str = [ 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]

        self.dy = calendar.monthcalendar(self.year, self.month)
        self.title = (self.month_str[self.month-1] + ", " + str(self.year) )

        layout = GridLayout(cols=7)

        # Llenar la fila superior con nombres de los días en negrita

        for d in self.day_str:
            b = Label(text = '[b]'+d+'[/b]' , markup=True )
            layout.add_widget(b)
        # # Llenar las fechas usando la lista de calendar.monthcalendar
        for wk in range(len(self.dy)):
            for kkk in range(0,7):
                dateOfWeek = self.dy[wk][kkk]
                if not dateOfWeek == 0:
                   eventoHoy = ColocarEvento(dateOfWeek,self.month_str[self.month-1], self.year  )
                   if eventoHoy:
                       b = kivy.uix.button.Button(text = str(dateOfWeek), background_color =(1, 128 / 255, 0, 0.8))
                       b.bind(on_release = self.date_selected)
                   else:
                       b = kivy.uix.button.Button(text = str(dateOfWeek))
                       b.bind(on_release = self.date_selected)
                else:
                    b = Label(text = '' )
                layout.add_widget(b)
        if self.root:
            self.root.clear_widgets()
        self.root.add_widget(layout)
        bottombox = BoxLayout(orientation = "horizontal", size_hint = (1,None), height = 50)
        bottombox.add_widget(kivy.uix.button.Button(text ='<', on_release = self.change_month))
        bottombox.add_widget(kivy.uix.button.Button(text ='>', on_release = self.change_month))
        self.root.add_widget(bottombox)


    def change_month(self, event):
        if event.text == '>':
            if self.month == 12:
                self.month = 1
                self.year = self.year + 1
            else:
                self.month = self.month + 1
        elif event.text == '<':
            if self.month == 1:
                self.month = 12
                self.year = self.year - 1
            else:
                self.month = self.month - 1

    def date_selected(self, event):
        self.day = int(event.text)
        #self.dismiss()

    def on_month(self, widget, event):
        self.create_calendar()

    def on_year(self, widget, event):
        self.create_calendar()

class Calendario(App):

    def build(self):
        # Target Month and Year to display
        self.popup = Calendar(month = mes, year = anno,
        size_hint=(None, None), size=(800, 600))
        #self.popup.bind(on_dismiss = self.on_dismiss)
        return kivy.uix.button.Button(text ="Ver Calendario", on_release = self.show_calendar)

    def show_calendar(self, event):
        self.popup.open()

    def on_dismiss(self, arg):
        pass

if __name__ == "__main__":
    Calendario().run()