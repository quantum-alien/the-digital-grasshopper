from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QSpinBox, QFormLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class SettingsDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки игры")
        self.setModal(True)
        self.setFixedSize(300, 200)
        
        layout = QFormLayout()
        
        self.rows_spin = QSpinBox()
        self.rows_spin.setRange(4, 8)
        self.rows_spin.setValue(6)
        layout.addRow("Количество строк:", self.rows_spin)
        
        self.cols_spin = QSpinBox()
        self.cols_spin.setRange(4, 8)
        self.cols_spin.setValue(6)
        layout.addRow("Количество столбцов:", self.cols_spin)
        
        self.grasshoppers_spin = QSpinBox()
        self.grasshoppers_spin.setRange(3, 8)
        self.grasshoppers_spin.setValue(6)
        layout.addRow("Количество кузнечиков:", self.grasshoppers_spin)
        
        buttons_layout = QHBoxLayout()
        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn = QPushButton("Отмена")
        self.cancel_btn.clicked.connect(self.reject)
        
        buttons_layout.addWidget(self.ok_btn)
        buttons_layout.addWidget(self.cancel_btn)
        
        layout.addRow(buttons_layout)
        self.setLayout(layout)
    
    def get_settings(self):
        return {
            'rows': self.rows_spin.value(),
            'cols': self.cols_spin.value(),
            'grasshoppers_count': self.grasshoppers_spin.value()
        }


class RulesDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Правила игры")
        self.setModal(True)
        self.setFixedSize(500, 400)
        
        layout = QVBoxLayout()
        
        self.web_view = QWebEngineView()
        html_content = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #2e8b57; }
                h2 { color: #2e8b57; margin-top: 20px; }
                p { line-height: 1.6; }
                ul { padding-left: 20px; }
                li { margin-bottom: 10px; }
                .highlight { background-color: #f0fff0; padding: 10px; border-radius: 5px; }
                .important { color: #ff4500; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Правила игры "Цифровой кузнечик"</h1>
            
            <div class="highlight">
                <h2>Цель игры</h2>
                <p>Переместите всех кузнечиков на новые позиции так, чтобы они не пересекались и каждый сделал ровно один ход!</p>
            </div>
            
            <h2>Основные правила</h2>
            <ul>
                <li><strong>Число = длина прыжка:</strong> Число на кузнечике показывает, на сколько клеток он должен прыгнуть (1, 2, 3 или 4)</li>
                <li><strong>Один ход на кузнечика:</strong> Каждого кузнечика можно переместить только один раз за уровень</li>
                <li><strong>Прямолинейное движение:</strong> Кузнечики прыгают только по вертикали или горизонтали</li>
                <li><strong>Свободный путь:</strong> На пути кузнечика не должно быть других кузнечиков</li>
            </ul>
            
            <h2>Особенности чисел</h2>
            <ul>
                <li><strong>1:</strong> Прыгает на 1 клетку - самый короткий ход</li>
                <li><strong>2:</strong> Прыгает на 2 клетки</li>
                <li><strong>3:</strong> Прыгает на 3 клетки</li>
                <li><strong>4:</strong> Прыгает на 4 клетки - самый длинный ход</li>
            </ul>
            
            <h2>Как играть</h2>
            <ul>
                <li>Выберите кузнечика кликом мыши</li>
                <li>Нажмите кнопку направления (↑↓←→) для перемещения</li>
                <li>Кузнечик прыгнет ровно на столько клеток, сколько показывает его число</li>
                <li>Планируйте последовательность ходов carefully!</li>
            </ul>
            
            <h2>Условия победы</h2>
            <ul>
                <li>Все кузнечики сделали по одному ходу</li>
                <li>Ни один кузнечик не вышел за пределы поля</li>
                <li>Кузнечики не пересекаются на новых позициях</li>
            </ul>
            
            <h2>Стратегия</h2>
            <ul>
                <li>Начинайте с кузнечиков с большими числами - им нужно больше пространства</li>
                <li>Кузнечики с числом 1 самые мобильные - оставляйте их на потом</li>
                <li>Продумывайте порядок ходов, чтобы не блокировать друг друга</li>
            </ul>
            
            <p class="important">Помните: последовательность ходов имеет решающее значение!</p>
        </body>
        </html>
        """
        self.web_view.setHtml(html_content)
        layout.addWidget(self.web_view)
        
        self.close_btn = QPushButton("Закрыть")
        self.close_btn.clicked.connect(self.accept)
        layout.addWidget(self.close_btn)
        
        self.setLayout(layout)