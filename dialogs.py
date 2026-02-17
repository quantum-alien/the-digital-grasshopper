from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QSpinBox, QFormLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class SettingsDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setModal(True)
        self.setFixedSize(300, 200)
        
        layout = QFormLayout()
        
        self.rows_spin = QSpinBox()
        self.rows_spin.setRange(4, 8)
        self.rows_spin.setValue(6)
        layout.addRow("Number of rows:", self.rows_spin)
        
        self.cols_spin = QSpinBox()
        self.cols_spin.setRange(4, 8)
        self.cols_spin.setValue(6)
        layout.addRow("Number of columns:", self.cols_spin)
        
        self.grasshoppers_spin = QSpinBox()
        self.grasshoppers_spin.setRange(3, 8)
        self.grasshoppers_spin.setValue(6)
        layout.addRow("Number of grasshoppers:", self.grasshoppers_spin)
        
        buttons_layout = QHBoxLayout()
        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn = QPushButton("Cancel")
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
        self.setWindowTitle("Game's rules")
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
            <h1>Rules of the Game "The Digital Grasshopper"</h1>
            
            <div class="highlight">
                <h2>Objective</h2>
                <p>Move all grasshoppers to new positions so they don't intersect and each one makes exactly one move!</p>
            </div>
            
            <h2>Basic Rules</h2>
            <ul>
                <li><strong>Number = jump length:</strong> The number on the grasshopper shows how many cells it should jump (1, 2, 3, or 4)</li>
                <li><strong>One move per grasshopper:</strong> Each grasshopper can only be moved once per level</li>
                <li><strong>Straight movement:</strong> Grasshoppers jump only vertically or horizontally</li>
                <li><strong>Clear path:</strong> There should be no other grasshoppers in the path</li>
            </ul>
            
            <h2>Number Characteristics</h2>
            <ul>
                <li><strong>1:</strong> Jumps 1 cell - the shortest move</li>
                <li><strong>2:</strong> Jumps 2 cells</li>
                <li><strong>3:</strong> Jumps 3 cells</li>
                <li><strong>4:</strong> Jumps 4 cells - the longest move</li>
            </ul>
            
            <h2>How to Play</h2>
            <ul>
                <li>Select a grasshopper by clicking with the mouse</li>
                <li>Press the direction button (↑↓←→) to move</li>
                <li>The grasshopper will jump exactly as many cells as its number indicates</li>
                <li>Plan the sequence of moves carefully!</li>
            </ul>
            
            <h2>Victory Conditions</h2>
            <ul>
                <li>All grasshoppers made one move each</li>
                <li>No grasshopper has gone beyond the field</li>
                <li>Grasshoppers do not intersect at new positions</li>
            </ul>
            
            <h2>Strategy</h2>
            <ul>
                <li>Start with grasshoppers with larger numbers - they need more space</li>
                <li>Grasshoppers with number 1 are the most mobile - save them for later</li>
                <li>Think through the order of moves to avoid blocking each other</li>
            </ul>
            
            <p class="important">Remember: the sequence of moves is crucial!</p>
        </body>
        </html>
        """
        self.web_view.setHtml(html_content)
        layout.addWidget(self.web_view)
        
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.accept)
        layout.addWidget(self.close_btn)
        
        self.setLayout(layout)