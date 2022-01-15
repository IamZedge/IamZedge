import kivy
from kivy.app import App
from kivy.core import window
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

Window.size = (650,400)


class Sellby_NL(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.9, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
  

        #add widgets to window

        #add image
        self.window.add_widget(Image(source="logo_small.png"))
        #add label
        self.greeting = Label(
                        text="Gib deinen Benutzernamen ein!",
                        font_size = 18,
                        color='#00FFCE'
                        )

        self.window.add_widget(self.greeting)
        #add Text
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20,20),
                    size_hint = (1, 0.5)
                    )
    
        self.window.add_widget(self.user)
        #add button
        self.button = Button(
                      text="Login",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#00FFCE',
                      )


        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hallo " + self.user.text + "!"




if __name__ == "__main__":
    Sellby_NL().run()