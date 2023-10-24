from PyQt6.QtCore import QUrl, QSize
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QFileDialog, QPushButton, QLabel, QVBoxLayout, QSpacerItem, \
    QSizePolicy, QMessageBox, QApplication, QDialog, QDialogButtonBox

import styles


class ChoicePath(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        self.paths = {
            "minecraft": self.config['paths'][self.config['os']].format(self.config['user']),
            "libraries": self.config['paths'][self.config['os']].format(self.config['user']) + "\\libraries",
            "version": self.config['paths'][self.config['os']].format(self.config['user']) + "\\versions"
        }

        self.main = QHBoxLayout()
        self.viewer = QLabel(f'   {self.paths["minecraft"]}   ')
        self.choicer = QPushButton("Выбрать путь")

        self.viewer.setFixedHeight(32)
        self.choicer.setFixedHeight(32)

        self.choicer.clicked.connect(self.choice_path)

        self.main.addWidget(self.viewer)
        self.main.addWidget(self.choicer)

        self.setLayout(self.main)

    def choice_path(self):
        parent = QFileDialog.getExistingDirectory(self, "Выбрать директорию", ".")

        if parent:
            self.paths = {
                "minecraft": parent,
                "libraries": parent + "\\libraries",
                "version": parent + "\\versions"
            }

            self.viewer.setText(f'   {self.paths["minecraft"]}   ')

    def get_paths(self):
        return self.paths


class StartUnpack(QPushButton):
    def __init__(self, callback):
        super().__init__()

        self.setText("Начать установку")
        self.clicked.connect(callback)

        self.setFixedHeight(32)


class Contacts(QWidget):
    def __init__(self):
        super().__init__()
        self.main = QHBoxLayout()

        self.urls = [
            QPushButton(""),
            QPushButton(""),
            QPushButton(""),
            QPushButton(""),
            QPushButton(""),
            QPushButton(""),
            QPushButton("")
        ]

        self.urls[0].clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/JessiXperience")))
        self.urls[0].setIcon(QIcon('res/icons/github.png'))
        self.urls[1].clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://t.me/JessiXperience")))
        self.urls[1].setIcon(QIcon('res/icons/telegram.png'))
        self.urls[2].clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://t.me/Sompetch")))
        self.urls[2].setIcon(QIcon('res/icons/telegram.png'))
        self.urls[3].clicked.connect(self.not_implemented)
        self.urls[3].setIcon(QIcon('res/icons/matrix.png'))
        self.urls[4].clicked.connect(self.not_implemented)
        self.urls[4].setIcon(QIcon('res/icons/youtube.png'))
        self.urls[5].clicked.connect(self.not_implemented)
        self.urls[5].setIcon(QIcon('res/icons/mastodon.png'))
        self.urls[6].clicked.connect(self.clipboard)
        self.urls[6].setIcon(QIcon('res/icons/email.png'))

        for index, widget in enumerate(self.urls):
            if index != 0:
                self.main.addItem(QSpacerItem(16, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))
            widget.setFixedSize(64, 64)
            widget.setIconSize(QSize(64, 64))
            widget.setStyleSheet(styles.Contacts.transparent)
            self.main.addWidget(widget)

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()

        self._hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._hbox.addItem(self._vbox)
        self._hbox.addItem(QSpacerItem(32, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding))

        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._vbox.addItem(self.main)
        self._vbox.addItem(QSpacerItem(0, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))

        self.setLayout(self._hbox)

    def not_implemented(self):
        try:
            message = QLabel("Ожидайте в скором времени!")
            layout = QHBoxLayout()
            layout.addWidget(message)

            dlg = QDialog(self)
            dlg.setWindowTitle("NewJessica")
            dlg.setLayout(layout)
            dlg.exec()
        except Exception as e:
            print(e)

    @staticmethod
    def clipboard():
        QApplication.clipboard().setText("JessiXperience@riseup.net")
