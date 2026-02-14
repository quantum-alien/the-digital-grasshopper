import random
from PyQt5.QtGui import QColor


class Game:
    
    def __init__(self, rows=6, cols=6):
        self._rows = rows
        self._cols = cols
        self.reset_game()
    
    @property
    def rows(self):
        return self._rows
    
    @property
    def cols(self):
        return self._cols
    
    @property
    def level_completed(self):
        return self._level_completed
    
    @property
    def game_over(self):
        return self._game_over
    
    @property
    def board(self):
        return [row[:] for row in self._board]
    
    @property
    def grasshoppers(self):
        return self._grasshoppers.copy()
    
    def reset_game(self):
        self._board = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._grasshoppers = []
        self._level_completed = False
        self._game_over = False
        self._generate_level()
    
    def _generate_level(self):
        self._grasshoppers = []
        
        numbers = [2, 2, 3, 3, 4, 4, 1, 1]
        random.shuffle(numbers)
        
        positions = []
        for i in range(self._rows):
            for j in range(self._cols):
                positions.append((i, j))
        
        random.shuffle(positions)
        
        max_grasshoppers = min(len(numbers), len(positions))
        for i in range(max_grasshoppers):
            row, col = positions[i]
            number = numbers[i]
            self._grasshoppers.append({'row': row, 'col': col, 'number': number, 'moved': False})
            self._board[row][col] = number
    
    def can_move_grasshopper(self, index, direction):
        if index < 0 or index >= len(self._grasshoppers):
            return False
        
        grasshopper = self._grasshoppers[index]
        if grasshopper['moved']:
            return False
        
        row, col = grasshopper['row'], grasshopper['col']
        number = grasshopper['number']
        
        if direction == 'up':
            new_row = row - number
            if new_row < 0:
                return False
            for r in range(row - 1, new_row - 1, -1):
                if self._board[r][col] != 0:
                    return False
            return True
        
        elif direction == 'down':
            new_row = row + number
            if new_row >= self._rows:
                return False
            for r in range(row + 1, new_row + 1):
                if self._board[r][col] != 0:
                    return False
            return True
        
        elif direction == 'left':
            new_col = col - number
            if new_col < 0:
                return False
            for c in range(col - 1, new_col - 1, -1):
                if self._board[row][c] != 0:
                    return False
            return True
        
        elif direction == 'right':
            new_col = col + number
            if new_col >= self._cols:
                return False
            for c in range(col + 1, new_col + 1):
                if self._board[row][c] != 0:
                    return False
            return True
        
        return False
    
    def move_grasshopper(self, index, direction):
        if not self.can_move_grasshopper(index, direction):
            return False
        
        grasshopper = self._grasshoppers[index]
        row, col = grasshopper['row'], grasshopper['col']
        number = grasshopper['number']
        
        self._board[row][col] = 0
        
        if direction == 'up':
            new_row = row - number
            grasshopper['row'] = new_row
        elif direction == 'down':
            new_row = row + number
            grasshopper['row'] = new_row
        elif direction == 'left':
            new_col = col - number
            grasshopper['col'] = new_col
        elif direction == 'right':
            new_col = col + number
            grasshopper['col'] = new_col
        
        grasshopper['moved'] = True
        self._board[grasshopper['row']][grasshopper['col']] = number
        
        self._check_level_completion()
        return True
    
    def _check_level_completion(self):
        all_moved = all(gh['moved'] for gh in self._grasshoppers)
        
        if all_moved:
            positions = [(gh['row'], gh['col']) for gh in self._grasshoppers]
            unique_positions = set(positions)
            
            if len(positions) == len(unique_positions):
                self._level_completed = True
            else:
                self._game_over = True
    
    def is_level_stuck(self):
        for i in range(len(self._grasshoppers)):
            if not self._grasshoppers[i]['moved']:
                for direction in ['up', 'down', 'left', 'right']:
                    if self.can_move_grasshopper(i, direction):
                        return False
        return True
    
    @staticmethod
    def get_grasshopper_color(number):
        colors = {
            1: QColor(255, 228, 181),
            2: QColor(173, 216, 230),
            3: QColor(144, 238, 144),
            4: QColor(255, 218, 185),
            5: QColor(221, 160, 221),
            6: QColor(240, 128, 128)
        }
        return colors.get(number, QColor(211, 211, 211))
    
    @staticmethod
    def get_text_color(number):
        return QColor(0, 0, 0)