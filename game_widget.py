from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont


class GameWidget(QWidget):
    
    def __init__(self, game, main_window, parent=None):
        super().__init__(parent)
        self.game = game
        self.main_window = main_window
        self.cell_size = 70
        self.selected_gh = -1
        self.setFixedSize(game.cols * self.cell_size + 20, game.rows * self.cell_size + 20)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        painter.fillRect(self.rect(), QColor(240, 240, 240))
        
        for i in range(self.game.rows):
            for j in range(self.game.cols):
                x = j * self.cell_size + 10
                y = i * self.cell_size + 10
                width = self.cell_size - 4
                height = self.cell_size - 4
                
                painter.setBrush(QColor(255, 255, 255))
                painter.setPen(QColor(200, 200, 200))
                painter.drawRect(x, y, width, height)
        
        for idx, gh in enumerate(self.game.grasshoppers):
            row, col = gh['row'], gh['col']
            number = gh['number']
            
            x = col * self.cell_size + 10
            y = row * self.cell_size + 10
            width = self.cell_size - 4
            height = self.cell_size - 4
            
            color = self.game.get_grasshopper_color(number)
            text_color = self.game.get_text_color(number)
            
            if idx == self.selected_gh:
                painter.setPen(QColor(255, 0, 0))
                painter.setBrush(QColor(255, 255, 255, 0))
                painter.drawRect(x - 2, y - 2, width + 4, height + 4)
            
            painter.setBrush(color)
            painter.setPen(QColor(150, 150, 150))
            painter.drawRoundedRect(x, y, width, height, 10, 10)
            
            painter.setPen(text_color)
            font = QFont("Arial", 16)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(x, y, width, height, Qt.AlignCenter, str(number))
            
            if gh['moved']:
                painter.setPen(QColor(0, 128, 0))
                painter.drawText(x + width - 20, y + 20, "✓")
    
    def mousePressEvent(self, event):
        col = (event.x() - 10) // self.cell_size
        row = (event.y() - 10) // self.cell_size
        
        if 0 <= row < self.game.rows and 0 <= col < self.game.cols:
            for idx, gh in enumerate(self.game.grasshoppers):
                if gh['row'] == row and gh['col'] == col and not gh['moved']:
                    self.selected_gh = idx
                    self.update()
                    self.main_window.update_status(f"Выбран кузнечик {gh['number']}")
                    return
            
            self.selected_gh = -1
            self.update()
            self.main_window.update_status("Выберите кузнечика")
    
    def move_selected(self, direction):
        if self.selected_gh >= 0:
            if self.game.move_grasshopper(self.selected_gh, direction):
                self.selected_gh = -1
                self.update()
                self.main_window.update_status("Ход выполнен")
                return True
            else:
                self.main_window.update_status("Невозможно выполнить ход")
        else:
            self.main_window.update_status("Сначала выберите кузнечика")
        return False