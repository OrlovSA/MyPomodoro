from kivy.core.window import Window


class Settings:
    Window.size = (340, 350)
    Window.minimum_width = 340
    Window.minimum_height = 350

    _resources_path = "app/resources"
    _data_path = f"{_resources_path}/data"

    sound_path = f"{_resources_path}/sound"
    image_path = f"{_resources_path}/images"
    files_data = f"{_data_path}/data.json"
    files_task = f"{_data_path}/task.json"
