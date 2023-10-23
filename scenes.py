from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton

import widgets


class Greeting(QWidget):
    def __init__(self, config):
        super().__init__()

        self.config = config
        print(self.config['paths'][self.config['os']].format(self.config['user']))

        self.main = QVBoxLayout()

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()

        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._vbox.addItem(self._hbox)
        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self._hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._hbox.addItem(self.main)
        self._hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.widgets = {
            "choice": {
                "path": widgets.ChoicePath(self.config)
            }
        }

        self.main.addWidget(self.widgets["choice"]["path"])

        self.setLayout(self._vbox)
