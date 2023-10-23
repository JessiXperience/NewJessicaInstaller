from PyQt6.QtWidgets import QHBoxLayout, QWidget, QFileDialog, QPushButton, QLabel

class ChoicePath(QWidget):
    def __init__(self, config, next_scene):
        super().__init__()
        self.config = config
        self.next_scene = next_scene

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
