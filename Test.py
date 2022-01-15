import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


Window.size = (350,120)


class TestApp(App):
    def build(self):
        self.cols = 1
        self.window = GridLayout()
        self.size_hint = (1,0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}






if __name__ == "__main__":
    TestApp().run()


