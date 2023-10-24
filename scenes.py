from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

import widgets


class Greeting(QWidget):
    def __init__(self, config, next_scene):
        super().__init__()

        self.config = config
        self.next_scene = next_scene

        self.main = QVBoxLayout()

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()
        self._footer = QVBoxLayout()

        self._vbox.addItem(QSpacerItem(0, 1280, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum))
        self._vbox.addLayout(self._hbox)
        self._footer.addItem(QSpacerItem(0, 1280, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._footer.addWidget(widgets.Splashier())
        self._vbox.addLayout(self._footer)

        self._hbox.addItem(QSpacerItem(300, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        self._hbox.addItem(self.main)
        self._hbox.addItem(QSpacerItem(300, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))

        self.widgets = {
            "paths": widgets.ChoicePath(self.config),
            "start": widgets.StartUnpack(self.next_scene)
        }

        self.main.addWidget(self.widgets["paths"])
        self.main.addWidget(self.widgets["start"])

        self.setLayout(self._vbox)

    def get_config(self):
        return self.widgets["paths"].get_config()

class Unpacker(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
