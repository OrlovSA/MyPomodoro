from datetime import datetime
import locale
import os
import pickle

from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from app import config


class HomeScreen(Screen):
    """основной скрин"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound7 = SoundLoader.load(f"{config.sound_path}/7.wav")
        self.sound8 = SoundLoader.load(f"{config.sound_path}/8.wav")
        self.sound1 = SoundLoader.load(f"{config.sound_path}/1.wav")
        self.sound2 = SoundLoader.load(f"{config.sound_path}/2.wav")
        self.sound4 = SoundLoader.load(f"{config.sound_path}/4.wav")
        self.sound5 = SoundLoader.load(f"{config.sound_path}/5.wav")
        self.sound6 = SoundLoader.load(f"{config.sound_path}/6.wav")
        self.time_30 = 1800
        self.time_25 = 1500
        self.time_5 = 300
        self.pbv = 100
        self.date = datetime.now()
        self.dt = datetime.now()
        self.time_log_task = 0
        self.time_log = 0
        self.pomodoro_pb = 0
        self.dtl = (
            f"Start {str(self.dt.hour).zfill(2)}:" f"{str(self.dt.minute).zfill(2)} / "
        )
        if locale.getdefaultlocale()[0] == "ru_RU":
            self.it1.hint_text = "Задача №1"
            self.it1.helper_text = "Опишите задачу."
            self.it2.hint_text = "Задача №2"
            self.it2.helper_text = "Опишите задачу."
            self.it3.hint_text = "Задача №3"
            self.it3.helper_text = "Опишите задачу."
            self.hb.text = "История"
            self.relaxation_5_text = "Хорошего отдыха!"
            self.finish_rest_5_text = "Закончить?"
            self.finish_rest_30_text = "Закончить большой перерыв?"
            self.relaxation_30_text = "Приятного большого отдыха!"
            self.distracted_text = "Не отвлекаться!"
            self.button_text_start = "Старт"
            self.button_text_complit = "Завершить"
            self.button_text_pause = "Пауза"
            self.button_text_reset = "Сбросить"
            self.but1.text = "Старт"
            self.but2.text = "Сбросить"
        else:
            self.relaxation_5_text = "Have a nice rest"
            self.finish_rest_5_text = "End break?"
            self.finish_rest_30_text = "Finish big break?"
            self.relaxation_30_text = "Enjoy your great rest!"
            self.distracted_text = "Do not be distracted!"
            self.button_text_start = "Start"
            self.button_text_complit = "Сompleted"
            self.button_text_pause = "Pause"
            self.button_text_reset = "Reset"

        if os.path.exists(config.files_data):
            with open(config.files_data, "rb") as file:
                data_new = pickle.load(file)
            self.time_log_task = data_new.get("time_log_task")
            self.time_log = data_new.get("time_log")
            self.pomodoro_pb = data_new.get("pomodoro_pb")
            self.dtl = data_new.get("dtl")
            self.date = data_new.get("data")
            self.it1.text = data_new.get("task")[0]
            self.it2.text = data_new.get("task")[1]
            self.it3.text = data_new.get("task")[2]

    def save_data(self):
        data = {
            "time_log_task": self.time_log_task,
            "time_log": self.time_log,
            "pomodoro_pb": self.pomodoro_pb,
            "dtl": self.dtl,
            "data": self.date,
            "task": [self.it1.text, self.it2.text, self.it3.text],
        }

        with open(config.files_data, "wb") as file:
            pickle.dump(data, file)

    def data_new(self):
        self.time_log_task = 0
        self.time_log = 0
        self.pomodoro_pb = 0
        self.dtl = (
            f"{self.button_text_start} {str(self.dt.hour).zfill(2)}:"
            f"{str(self.dt.minute).zfill(2)} / "
        )
        self.date = self.dt.date()
        self.it1.text = ""
        self.it2.text = ""
        self.it3.text = ""
        self.lb1.text = ""
        self.pb.value = 0
        self.save_data()
        self.check1.active = False
        self.check2.active = False
        self.check3.active = False

    def timer_new(self, dt):
        if self.time_25 == 1500:
            self.sound1.play()
        if self.time_25 == 300:
            self.sound4.play()
        if self.time_25 == 4:
            self.sound5.play()
        if self.time_25 != 0:
            self.time_25 -= 1
            self.time_log_task += 1
            self.time_log += 1
            self.pomodoro_pb += 0.01666
            hl = str(self.time_log // 3600).zfill(2)
            ml = str((self.time_log % 3600) // 60).zfill(2)
            m = str((self.time_25 % 3600) // 60).zfill(2)
            s = str((self.time_25 % 3600) % 60).zfill(2)
            self.pb.value = self.pomodoro_pb
            self.lb.text = f"{m}:{s}"
            self.lb1.text = f"{self.dtl}{hl}:{ml}"
        else:
            if self.pomodoro_pb < 100:
                if self.time_5 == 300:
                    Window.set_title(self.relaxation_5_text)
                    Window.restore()
                    self.sound1.play()
                    self.pb.color = 0.31, 0.78, 0.47, 1
                    self.lb.color = 0.31, 0.78, 0.47, 1
                    self.but2.text = self.finish_rest_5_text
                    self.but1.text_color = 0.5, 0.5, 0.5, 1
                    self.but1.text = "---"
                if self.time_5 != 0:
                    self.time_5 -= 1
                    self.pbv -= 0.333
                    m = str((self.time_5 % 3600) // 60).zfill(2)
                    s = str((self.time_5 % 3600) % 60).zfill(2)
                    self.pb.value = self.pbv
                    self.lb.text = f"{m}:{s}"
                else:
                    Window.restore()
                    self.sound1.play()
                    self.timer_stop()
            else:
                if self.time_30 == 1800:
                    Window.set_title(self.relaxation_30_text)
                    Window.restore()
                    self.sound1.play()
                    self.pb.color = 0.31, 0.78, 0.47, 1
                    self.lb.color = 0.31, 0.78, 0.47, 1
                    self.but2.text = self.finish_rest_30_text
                    self.but1.text_color = 0.5, 0.5, 0.5, 1
                    self.but1.text = "---"
                if self.time_30 != 0:
                    self.time_30 -= 1
                    self.pbv -= 0.0555
                    m = str((self.time_30 % 3600) // 60).zfill(2)
                    s = str((self.time_30 % 3600) % 60).zfill(2)
                    self.pb.value = self.pbv
                    self.lb.text = f"{m}:{s}"
                else:
                    Window.restore()
                    self.sound1.play()
                    self.timer_stop()

    def timer_pause(self):
        self.sound2.play()
        Window.set_title(self.distracted_text)
        self.but1.text = self.button_text_start
        self.pb.color = 0.5, 0.5, 0.5, 1
        self.lb.color = 0.5, 0.5, 0.5, 1
        Clock.unschedule(self.timer_new)
        Clock.schedule_interval(self.timer_pause_plus, 1)

    def timer_pause_plus(self, dt):
        if self.time_25 != 1500:
            self.time_25 += 1
            m = str((self.time_25 % 3600) // 60).zfill(2)
            s = str((self.time_25 % 3600) % 60).zfill(2)
            self.sound6.play()
            self.lb.text = f"{m}:{s}"
        else:
            Window.restore()
            self.sound1.play()
            self.timer_stop()

    def timer_run(self):
        self.sound6.stop()
        Clock.unschedule(self.timer_pause_plus)
        self.sound2.play()
        Window.set_title(self.it1.text)
        self.pb.color = 1, 1, 0.0, 1
        self.lb.color = 1, 1, 1, 1
        self.but2.text = self.button_text_complit
        self.but2.text_color = 1, 1, 1, 1
        self.but1.text = self.button_text_pause
        Clock.schedule_interval(self.timer_new, 1)
        self.save_data()

    def timer_stop(self):
        if self.check1.active:
            self.check1.active = False
            self.it1.text = ""
            if not self.check2.active:
                self.it1.text = self.it2.text
                self.it2.text = ""
            else:
                self.check2.active = False
                self.it2.text = ""
                if not self.check3.active:
                    self.it1.text = self.it3.text
                    self.it3.text = ""
                else:
                    self.it3.text = ""
            if not self.check3.active:
                self.it2.text = self.it3.text
                self.it3.text = ""
            else:
                self.check3.active = False

        self.it1.helper_text = ""
        self.it2.helper_text = ""
        self.it3.helper_text = ""
        self.sound6.stop()
        Clock.unschedule(self.timer_pause_plus)
        Window.set_title("Pomodoro task")
        self.sound2.play()
        Clock.unschedule(self.timer_new)
        self.but1.text = self.button_text_start
        self.but1.text_color = 1, 1, 1, 1
        self.but2.text = self.button_text_reset
        self.but2.text_color = 1, 1, 1, 1
        self.pb.value = self.pomodoro_pb
        self.lb.text = "25:00"
        self.pb.color = 1, 1, 0.0, 1
        self.lb.color = 1, 1, 1, 1
        self.time_30 = 1800
        self.time_25 = 1500
        self.time_5 = 300
        self.pbv = 100
        self.save_data()

    def trig_button_1(self):
        if self.but1.text == self.button_text_start:
            self.timer_run()
        elif self.but1.text == self.button_text_pause:
            self.timer_pause()
        else:
            self.sound8.play()

    def trig_button_2(self):
        if (
            self.but2.text == self.button_text_complit
            or self.but2.text == self.finish_rest_5_text
        ):
            self.timer_stop()
        elif self.but2.text == self.finish_rest_30_text:
            self.timer_stop()
            self.pomodoro_pb = 0.04
        else:
            self.data_new()

    def trig_chec(self, cb, lb):
        if cb.active and lb.text:
            self.sound7.play()
            h = str(self.time_log_task // 3600).zfill(2)
            m = str((self.time_log_task % 3600) // 60).zfill(2)
            s = str((self.time_log_task % 3600) % 60).zfill(2)
            lb.helper_text = f"{h}:{m}:{s}"
            lb.helper_text_mode = "persistent"
            self.time_log_task = 0
            t_data = self.dt.date()
            if os.path.exists(config.files_task):
                with open(config.files_task, "rb") as file:
                    data = pickle.load(file)
                    if data[-1][0] == t_data:
                        data[-1][1].append([lb.text, f"{h}:{m}:{s}"])
                    else:
                        data.append([t_data, [[lb.text, f"{h}:{m}:{s}"]]])
            else:
                data = [[t_data, [[lb.text, f"{h}:{m}:{s}"]]]]

            with open(config.files_task, "wb") as file:
                pickle.dump(data, file)
        else:
            cb.active = False
            self.sound8.play()
            lb.helper_text = ""
            lb.text = ""
