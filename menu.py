from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
import os

from kivy.core.window import Window
Window.size = (800, 600)

try:
    import kivymd
except ImportError:
    print("brak biblioteki")
    os.system('python -m pip install kivymd')
    import kivymd

class Menu(MDScreen):
    pass

class App(MDApp):
    def build(self):
        self.title = "SNAKEPRO"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"

        return Builder.load_file("menu.kv")

App().run()
