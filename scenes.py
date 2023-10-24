import os
import threading
import time

import requests
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QProgressBar

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

        self.main = QProgressBar()
        self.main.setValue(1)
        self.main.setTextVisible(True)
        self.main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._vbox = QVBoxLayout()
        self._hbox = QHBoxLayout()
        self._footer = QVBoxLayout()

        self._vbox.addItem(QSpacerItem(0, 1280, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum))
        self._vbox.addLayout(self._hbox)
        self._footer.addItem(QSpacerItem(0, 1280, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        self._footer.addWidget(widgets.Splashier())
        self._vbox.addLayout(self._footer)

        self._hbox.addItem(QSpacerItem(300, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        self._hbox.addWidget(self.main)
        self._hbox.addItem(QSpacerItem(300, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))

        self.setLayout(self._vbox)

        self.loading = threading.Thread(target=self.loader)
        self.loading.start()



    def loader(self):
        self.main.setFormat("Loading...")
        time.sleep(0.5)

        username = 'JessiXperience'
        reponame = 'NewJessicaInstaller'

        response = requests.get(f'https://api.github.com/repos/{username}/{reponame}/branches/files')
        branch_data = response.json()

        files = []

        if 'commit' not in branch_data:
            self.main.setFormat(f"Произошла ошибка при загрузке. Пожалуйста, обновите установщик.")
            return
        else:
            commit_sha = branch_data['commit']['sha']
            tree_url = f'https://api.github.com/repos/{username}/{reponame}/git/trees/{commit_sha}?recursive=1'
            tree_response = requests.get(tree_url)
            tree_data = tree_response.json()

            if 'tree' not in tree_data:
                self.main.setFormat(f"Произошла ошибка при загрузке. Пожалуйста, обновите установщик.")
                return
            else:
                _files = [file['path'] for file in tree_data['tree'] if file['type'] == 'blob']
                for file in _files:
                    if file.startswith("libraries"):
                        files.append((file, self.config["paths"]["libraries"] + file))
                    elif file.startswith("version"):
                        files.append((file, self.config["paths"]["versions"] + file.replace("version", "NewJessica 5.0.2", 1)))

        time.sleep(0.5)

        for file, directory in files:
            if not threading.main_thread().is_alive():
                break

            self.main.setFormat(f"Download | {file}")

            os.makedirs(os.path.dirname(directory), exist_ok=True)

            raw_url = f'https://raw.githubusercontent.com/{username}/{reponame}/files/{file}'

            response = requests.get(raw_url)

            if response.status_code == 200:
                with open(directory, 'wb+') as f:
                    f.write(response.content)
            else:
                self.main.setFormat(f"Произошла ошибка при загрузке. Пожалуйста, обновите установщик.")
                break
        else:
            self.main.setFormat(f"Загрузка завершена!")
            return

        self.main.setValue(100)
