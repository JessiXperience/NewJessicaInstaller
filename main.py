import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

import scenes
import styles


class MainWindow(QMainWindow):
    @staticmethod
    def config_loader():
        import getpass
        import json
        import os

        path = "./config.json"

        file = open(path, "r")

        config = json.load(file)

        config['user'] = getpass.getuser()
        config['os'] = os.name

        try:
            config['paths'] = config['paths'][config['os']]
        except KeyError:
            print("Ваша операционная система не поддерживается!")
            input()
            exit(0)

        for key, value in config['paths'].items():
            config['paths'][key] = value.format(user=config['user'])

        return config


    def __init__(self):
        super().__init__()
        self.setStyleSheet(styles.Scenes.greeting)
        self.resize(1280, 720)
        self.setFixedSize(1280, 720)
        self.setWindowTitle("NewJessica Installer")

        self.config = self.config_loader()

        self.central = scenes.Greeting(self.config, self.unpack)

        self.setCentralWidget(self.central)

    def unpack(self):
        self.config = self.central.get_config()

        self.central = scenes.Unpacker(self.config)
        self.setCentralWidget(self.central)

    def end(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
