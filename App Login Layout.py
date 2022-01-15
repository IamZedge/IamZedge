import kivy
from kivy.app import App
from kivy.core import window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.button import Button

# change window size
Window.size = (650,200)

# with builder you add the cavey (kv) file:
Builder.load_string("""
<Login>:
    ben: ben.text
    pw: passwort.text
    knopf: btn

    GridLayout:
        cols: 1
        size: root.width, root.height
        GridLayout:
            cols: 2
            Label:
                text: "Benutzername"
                font_size: 40
            TextInput:
                id: ben
                multiline: False
            Label:
                text: "Passwort"
                font_size: 40
            TextInput:
                password: True
                id: passwort
                multiline: False
                font_size: 40
        Button:
            text:"Anmelden"
            id: btn
            size_hint: (1.,0.5)
            font_size: 40
            on_release:
                root.loginPopup()
                root.manager.current = "Startseite" if passwort.text == "1234" and ben.text == "bunning" else "login"
                root.manager.transition.direction = "left"            


# here is our another window
<Startseite>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Startseite"
            font_size: 40
        Button:
            text: "Zurück zum Login"
            font_size: 40
            on_release:
                root.loginPopup()
                root.manager.current = "Startseite" if Button = "Startseite" go to "second_page"
                root.manager.transition.direction = "right"

<second_page>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "Zweite Seite"
            font_size: 40
        Button:
            text: "Weiter zum Login"
            font_size: 40
            on_release:
                root.manager.current = "second_page"
                root.manager.transition.direction = "right"

""")
# thats our Login failure screen
class Login(Screen):
    email = StringProperty()
    pw = StringProperty()
    knopf = ObjectProperty()
    # here comes our syntax failure popup window
    def loginPopup(self):
        if self.ben == "" or self.pw == "":
            popup = Popup(title='Fehler!',
            content = Label(text="Es wurde kein Passwort oder E-mail eingegeben!"),
            size_hint=(None,None),size=(800,150))
            popup.open()
        else:
            if self.ben == "bunning" and self.pw == "1234":
                self.knopf.background_color = [0., 1., 0., 1.]
            else:
                self.knopf.background_color = [1., 0., 0., 1.]

class Startseite(Screen):
    pass

class second_page(Screen):
    pass


ms = ScreenManager()
ms.add_widget(Login(name='login'))
ms.add_widget(Startseite(name='Startseite'))
ms.add_widget(second_page(name='second_page'))

class StartApp(App):
    def build(self):
        return ms



if __name__ == "__main__":
    StartApp().run()
