from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import os
#import main

try:
    import kivy
except ImportError:
    print("brak biblioteki")
    os.system('python -m pip install kivy')
    import kivy

class MenuScreen(Screen):
    pass

class ScoreboardScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class Manager(ScreenManager):
    pass
    
kv = Builder.load_file("menu.kv")

class Menu(App):
    def build(self):
        return kv

Menu().run()


