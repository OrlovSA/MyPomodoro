import locale
import os
import pickle

from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem, TwoLineListItem

from app import config
from app.screens.home.home import HomeScreen


class HistoryScreen(HomeScreen, Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if locale.getdefaultlocale()[0] == "ru_RU":
            self.but3.text = "Назад"
            self.but4.text = "Удалить"
            self.no_history_text = "Нет истории"
        else:
            self.no_history_text = "No history"

    def rid(self):
        self.manager.current = "history"
        self.lost_history.clear_widgets(children=None)
        if os.path.exists(config.files_task):
            with open(config.files_task, "rb") as file:
                data = pickle.load(file)
            for i in data:
                self.lost_history.add_widget(
                    OneLineListItem(text_color=[1, 1, 1, 1], text=f"{i[0]}")
                )
                for n in i[1]:
                    self.lost_history.add_widget(
                        TwoLineListItem(
                            text=f"{n[0]}",
                            text_color=[1, 1, 1, 1],
                            secondary_text_color=[1, 1, 1, 1],
                            secondary_text=f"{n[1]}",
                        )
                    )
        else:
            self.lost_history.add_widget(
                OneLineListItem(text_color=[1, 1, 1, 1], text=self.no_history_text)
            )

    def reset(self):
        if os.path.exists(config.files_task):
            os.remove(config.files_task)
            self.lost_history.clear_widgets(children=None)
            self.lost_history.add_widget(
                OneLineListItem(text_color=[1, 1, 1, 1], text=self.no_history_text)
            )
        else:
            self.sound8.play()
