from kivy.config import Config as KivyConfig
KivyConfig.set("input", "mouse", "mouse,multitouch_on_demand")
KivyConfig.set("graphics", "resizable", False)
KivyConfig.set("graphics", "width", "300")
KivyConfig.set("graphics", "height", "350")

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder

from app.screens.home.home import HomeScreen
from app.screens.history.history import HistoryScreen
from app import config


class PomodoroApp(MDApp):
    title = "Pomodoro task"
    icon = f"{config.image_path}/pomodoro.jpg"

    def build(self):
        Builder.load_file("app/screens/home/home.kv")
        Builder.load_file("app/screens/history/history.kv")

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(HistoryScreen(name='history'))
        return sm


if __name__ == "__main__":
    PomodoroApp().run()
