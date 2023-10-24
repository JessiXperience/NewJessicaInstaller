from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

import widgets


class Greeting(QWidget):
    def __init__(self, config, next_scene):
        super().__init__()

        self.config = config
        self.next_scene = next_scene
        print(self.config['paths'][self.config['os']].format(self.config['user']))

        self.main = QVBoxLayout()

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()

        self._hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._hbox.addItem(self._vbox)
        self._hbox.addWidget(widgets.Contacts())

        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._vbox.addItem(self.main)
        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.widgets = {
            "choice path": widgets.ChoicePath(self.config),
            "start": widgets.StartUnpack(self.next_scene)
        }

        self.main.addWidget(self.widgets["choice path"])
        self.main.addWidget(self.widgets["start"])

        self.setLayout(self._hbox)

    def get_paths(self):
        return self.widgets["choice path"].get_paths()

class Unpacker(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        print(self.config)
