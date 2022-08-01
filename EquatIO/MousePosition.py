from talon import ctrl
import os

class MousePosition:
    STRING_START = '('
    STRING_ENDING = ')'
    COORDINATE_SEPARATOR = ', '
    def __init__(self, horizontal: int, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical
    
    def get_horizontal(self):
        return self.horizontal
    def get_vertical(self):
        return self.vertical
    
    def __add__(self, other):
        result = MousePosition(0, 0)
        result += self
        result += other
        return result
    def __iadd__(self, other):
        self.horizontal += other.horizontal
        self.vertical += other.vertical
        return self
    def __sub__(self, other):
        result = MousePosition(0, 0)
        result += self
        result -= other
        return result
    def __isub__(self, other):
        self.horizontal -= other.horizontal
        self.vertical -= other.vertical
        return self

    def __str__(self) -> str:
        return MousePosition.STRING_START + str(self.horizontal) + MousePosition.COORDINATE_SEPARATOR \
        + str(self.vertical) + MousePosition.STRING_ENDING

    #assumes that the text properly represents a mouse position object
    @staticmethod
    def from_text(text: str):
        horizontal_start = text.index(MousePosition.STRING_START) + 1
        horizontal_ending = text.index(MousePosition.COORDINATE_SEPARATOR)
        horizontal = int(text[horizontal_start : horizontal_ending])
        vertical_start = horizontal_ending + 1
        vertical_ending = text.index(MousePosition.STRING_ENDING)
        vertical = int(text[vertical_start : vertical_ending])
        return MousePosition(horizontal, vertical)

class MousePositionFile:
    def __init__(self, folder: str, name: str):
        self.folder = folder
        self.name = name
        self._initialize_file_if_nonexistent()
        self.position = self._retrieve_position()
        
    def get(self):
        return self.position
        
    def set(self, position: MousePosition):
        self.position = position
        self._store_position()
    
    def set_to_current_mouse_position(self):
        horizontal, vertical = ctrl.mouse_pos()
        position = MousePosition(horizontal, vertical)
        self.set(position)
    
    def _store_position(self):
        with open(self.get_path(), 'w') as position_file:
            position_text = str(self.position)
            position_file.write(position_text)
    
    def _retrieve_position(self):
        with open(self.get_path, 'r') as position_file:
            position_text = position_file.readline().rstrip('\n\r')
            self.position = MousePosition.from_text(position_text)
    
    def get_path(self):
        return os.path.join(self.folder, self.name)
    
    def _initialize_file_if_nonexistent(self):
        if not os.path.exists(self.get_path()):
            self._make_directory_if_nonexistent()
            self.set(MousePosition(0, 0))
    
    def _make_directory_if_nonexistent(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
