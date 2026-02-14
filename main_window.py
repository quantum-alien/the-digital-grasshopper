from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel,
                             QMessageBox)
from PyQt5.QtCore import Qt

from game import Game
from game_widget import GameWidget
from dialogs import SettingsDialog, RulesDialog


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.game = Game()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Цифровой кузнечик")
        self.setFixedSize(700, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        control_layout = QHBoxLayout()
        
        self.status_label = QLabel("Выберите кузнечика для начала")
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        control_layout.addWidget(self.status_label)
        
        control_layout.addStretch()
        
        self.new_level_btn = QPushButton("Новый уровень")
        self.new_level_btn.clicked.connect(self.new_level)
        control_layout.addWidget(self.new_level_btn)
        
        self.restart_btn = QPushButton("Перезапуск")
        self.restart_btn.clicked.connect(self.restart_level)
        control_layout.addWidget(self.restart_btn)
        
        self.settings_btn = QPushButton("Настройки")
        self.settings_btn.clicked.connect(self.show_settings)
        control_layout.addWidget(self.settings_btn)
        
        self.rules_btn = QPushButton("Правила")
        self.rules_btn.clicked.connect(self.show_rules)
        control_layout.addWidget(self.rules_btn)
        
        layout.addLayout(control_layout)
        
        self.game_widget = GameWidget(self.game, self)
        layout.addWidget(self.game_widget, alignment=Qt.AlignCenter)
        
        button_layout = QHBoxLayout()
        
        self.up_btn = QPushButton("↑ Вверх")
        self.up_btn.clicked.connect(lambda: self.make_move('up'))
        button_layout.addWidget(self.up_btn)
        
        self.down_btn = QPushButton("↓ Вниз")
        self.down_btn.clicked.connect(lambda: self.make_move('down'))
        button_layout.addWidget(self.down_btn)
        
        self.left_btn = QPushButton("← Влево")
        self.left_btn.clicked.connect(lambda: self.make_move('left'))
        button_layout.addWidget(self.left_btn)
        
        self.right_btn = QPushButton("→ Вправо")
        self.right_btn.clicked.connect(lambda: self.make_move('right'))
        button_layout.addWidget(self.right_btn)
        
        layout.addLayout(button_layout)
    
    def make_move(self, direction):
        if self.game.level_completed or self.game.game_over:
            return
        
        if self.game_widget.move_selected(direction):
            if self.game.level_completed:
                QMessageBox.information(self, "Победа!", "Уровень пройден! Все кузнечики размещены корректно.")
                self.update_status("Уровень пройден!")
            elif self.game.game_over:
                QMessageBox.warning(self, "Конфликт", "Кузнечики пересеклись! Начните уровень заново.")
                self.update_status("Конфликт позиций")
            elif self.game.is_level_stuck():
                QMessageBox.warning(self, "Тупик", "Невозможно сделать ход! Начните уровень заново.")
                self.update_status("Тупиковая ситуация")
    
    def update_status(self, message):
        self.status_label.setText(message)
    
    def new_level(self):
        self.game.reset_game()
        self.game_widget.selected_gh = -1
        self.game_widget.update()
        self.update_status("Новый уровень начат")
    
    def restart_level(self):
        self.game.reset_game()
        self.game_widget.selected_gh = -1
        self.game_widget.update()
        self.update_status("Уровень перезапущен")
    
    def show_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            settings = dialog.get_settings()
            self.game = Game(settings['rows'], settings['cols'])
            self.game_widget.game = self.game
            self.game_widget.setFixedSize(
                self.game.cols * self.game_widget.cell_size + 20,
                self.game.rows * self.game_widget.cell_size + 20
            )
            self.new_level()
    
    def show_rules(self):
        dialog = RulesDialog(self)
        dialog.exec_()