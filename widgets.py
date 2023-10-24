from PyQt6.QtCore import QUrl, QSize
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QFileDialog, QPushButton, QLabel, QVBoxLayout, QSpacerItem, \
    QSizePolicy, QApplication, QDialog

import styles


class ChoicePath(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        self.main = QVBoxLayout()

        self.libraries = QHBoxLayout()
        self.versions = QHBoxLayout()

        self.viewer_versions = QLabel(f'   {self.config["paths"]["versions"]}   ')
        self.viewer_libraries = QLabel(f'   {self.config["paths"]["libraries"]}   ')
        self.choicer_versions = QPushButton("Выбрать путь до версий")
        self.choicer_libraries = QPushButton("Выбрать путь до библиотек")

        self.viewer_versions.setFixedHeight(32)
        self.viewer_libraries.setFixedHeight(32)
        self.choicer_versions.setFixedHeight(32)
        self.choicer_versions.setFixedWidth(192)
        self.choicer_libraries.setFixedHeight(32)
        self.choicer_libraries.setFixedWidth(192)

        self.choicer_versions.clicked.connect(self.choice_versions)
        self.choicer_libraries.clicked.connect(self.choice_libraries)

        self.libraries.addWidget(self.viewer_libraries)
        self.libraries.addWidget(self.choicer_libraries)

        self.versions.addWidget(self.viewer_versions)
        self.versions.addWidget(self.choicer_versions)

        self.main.addLayout(self.versions)
        self.main.addLayout(self.libraries)

        self.setLayout(self.main)

    def choice_versions(self):
        parent = QFileDialog.getExistingDirectory(self, "Выбрать директорию версий", ".")

        if parent:
            self.config["paths"]["versions"] = parent
            self.viewer_versions.setText(f'   {self.config["paths"]["versions"]}   ')

    def choice_libraries(self):
        parent = QFileDialog.getExistingDirectory(self, "Выбрать директорию библиотек", ".")

        if parent:
            self.config["paths"]["libraries"] = parent
            self.viewer_libraries.setText(f'   {self.config["paths"]["libraries"]}   ')

    def get_config(self):
        return self.config


class StartUnpack(QPushButton):
    def __init__(self, callback):
        super().__init__()

        self.setText("Начать установку")
        self.clicked.connect(callback)

        self.setFixedHeight(32)


class Splashier(QWidget):
    def __init__(self):
        super().__init__()

        self._hbox = QHBoxLayout()
        self._vbox = QVBoxLayout()

        self._vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum))
        self._vbox.addWidget(Contacts())
        self._vbox.addItem(QSpacerItem(0, 32, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))

        self._hbox.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        self._hbox.addLayout(self._vbox)
        self._hbox.addItem(QSpacerItem(32, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding))

        self.setLayout(self._hbox)

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

        self._hbox = QHBoxLayout()

        self._hbox.addItem(QSpacerItem(1280, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        self._hbox.addItem(self.main)
        self._hbox.addItem(QSpacerItem(32, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum))

        self.setLayout(self._hbox)

    def not_implemented(self):
        message = QLabel("Ожидайте в скором времени!")
        layout = QHBoxLayout()
        layout.addWidget(message)

        dlg = QDialog(self)
        dlg.setWindowTitle("NewJessica")
        dlg.setLayout(layout)
        dlg.exec()

    @staticmethod
    def clipboard():
        QApplication.clipboard().setText("JessiXperience@riseup.net")
