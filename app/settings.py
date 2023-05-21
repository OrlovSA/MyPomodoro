from kivy.core.window import Window


class Settings:
    Window.size = (300, 350)
    Window.minimum_width = 300
    Window.minimum_height = 350

    _resources_path = "app/resources"
    _data_path = f"{_resources_path}/data"

    sound_path = f"{_resources_path}/sound"
    image_path = f"{_resources_path}/image"
    files_data = f"{_data_path}/data.json"
    files_task = f"{_data_path}/task.json"
