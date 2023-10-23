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

        return config


    def __init__(self):
        super().__init__()
        self.setStyleSheet(styles.Scenes.greeting)
        self.resize(1280, 720)

        self.config = self.config_loader()

        self.central = scenes.Greeting(self.config)

        self.setCentralWidget(self.central)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
