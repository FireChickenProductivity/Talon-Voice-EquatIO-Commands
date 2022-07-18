from talon import Module, actions
    
mod = Module()


@mod.action_class
class Actions:
    def equatio_build_matrix_with_boundary(boundary: tuple, rows: int, columns: int):
        '''Builds an empty matrix with the specified dimensions in equatio'''
        matrix_text = boundary[0] + empty_matrix_text(rows, columns) + boundary[1]
        actions.user.equatio_paste_text(matrix_text)
        go_to_matrix_first_entry_from_matrix_right()
    def equatio_build_matrix_with_square_boundary(rows: int, columns: int):
        '''Builds an empty matrix with square boundaries'''
        actions.user.equatio_build_matrix_with_boundary(equatio_matrix_boundary(['square']), rows, columns)
    def equatio_build_column_matrix_with_boundary(boundary: tuple, rows: int, columns: int):
        '''Builds a matrix out of columns with the specified dimensions and boundaries'''
        matrix_text = boundary[0]
        column_text = empty_matrix_text(rows, 1)
        for column in range(columns):
            matrix_text += column_text
        matrix_text += boundary[1]
        actions.user.equatio_paste_text(matrix_text)
        go_to_matrix_first_entry_from_matrix_right()
    def equatio_build_matrix_augment(rows: int, columns: int):
        '''Builds a matrix augment with specified dimensions'''
        make_augment_line_with_height(rows)
        paste_empty_matrix(rows, columns)
        go_to_empty_matrix_first_entry_from_right_but_within_container(rows, columns)
    def equatio_build_column_matrix_with_square_boundary(rows: int, columns: int):
        '''Builds a matrix out of columns with square boundaries'''
        actions.user.equatio_build_column_matrix_with_boundary(equatio_matrix_boundary(['square']), rows, columns)
    def equatio_go_to_matrix_entry(row: int, column: int):
        '''Goes to the specified matrix entry'''
        rows, columns = get_matrix_dimensions()
        if row > rows or column > columns:
            actions.key('left')
            actions.key('right')
            return 
        horizontal_movement_amount = compute_how_much_to_move_horizontally_to_reach_entry_given_column_count_and_target(columns, [row, column])
        actions.key('left')
        actions.key('right')
        entry_move_horizontally_by_amount(horizontal_movement_amount)
    def equatio_go_to_matrix_first_entry():
        '''Goes to the first entry of the matrix'''
        go_to_matrix_first_entry()
    def equatio_go_to_matrix_last_entry():
        '''Goes to the last entry of the matrix'''
        go_to_matrix_last_entry()
    def equatio_go_to_matrix_next_entry():
        '''Goes to the next entry of the matrix'''
        go_to_next_matrix_entry()
    def equatio_go_to_matrix_previous_entry():
        '''Goes to the previous entry of the matrix'''
        go_to_previous_matrix_entry()
    def equatio_leave_matrix_left():
        '''Exits the matrix to the left'''
        leave_matrix_left()
    def equatio_leave_matrix_right():
        '''Exits the matrix to the right'''
        leave_matrix_right()
    

PIPES_MATRIX_BOUNDARIES = ('|\\left|', '|\\right|')
PIPE_MATRIX_BOUNDARIES = ('|', '|')
SQUARE_MATRIX_BOUNDARIES = ('[', ']')
MATRIX_BOUNDARIES = {
    'pipe': PIPE_MATRIX_BOUNDARIES,
    'bar': PIPE_MATRIX_BOUNDARIES,
    'pipes': PIPES_MATRIX_BOUNDARIES,
    'bars': PIPES_MATRIX_BOUNDARIES,
    'square': SQUARE_MATRIX_BOUNDARIES,
    'bracket': SQUARE_MATRIX_BOUNDARIES,
    'brace': (r'\{', r'\}'),
    'paren': ('(', ')'),
}

MATRIX_BOUNDARY_START = '\\left'
MATRIX_BOUNDARY_ENDING = '\\right'

@mod.capture(rule = 'pipe|bar|square|bracket|brace|paren|pipes|bars')
def equatio_matrix_boundary(input) -> tuple:
    boundaries = MATRIX_BOUNDARIES[input[0]]
    return (MATRIX_BOUNDARY_START + boundaries[0], MATRIX_BOUNDARY_ENDING + boundaries[1])

def empty_matrix_text(rows, columns):
    EmptyMatrix = Matrix(rows, columns)
    return EmptyMatrix.text()

def paste_empty_matrix(rows, columns):
    matrix_text = empty_matrix_text(rows, columns)
    actions.user.equatio_paste_text(matrix_text)

def make_augment_line_with_height(height):
    AugmentLineMatrix = Matrix(height, 1)
    AugmentLineMatrix.fill_with_text('\\mid')
    actions.user.equatio_paste_text(AugmentLineMatrix.text())

def go_to_matrix_first_entry_from_matrix_right():
    actions.key('left')
    actions.key('home')
    actions.key('right')

def go_to_empty_matrix_first_entry_from_right_but_within_container(rows, columns):
    for column in range(columns):
        actions.edit.left()
    for row in range(rows):
        actions.edit.up()

def go_to_matrix_first_entry():
    select_current_matrix()
    actions.key('left')
    actions.key('right')

def go_to_matrix_last_entry():
    select_current_matrix()
    actions.key('right')
    actions.key('left')

def go_to_next_matrix_entry():
    actions.key('escape')

def go_to_previous_matrix_entry():
    actions.key('home')
    actions.key('shift-escape')

def leave_matrix_left():
    select_current_matrix()
    actions.key('shift-escape:2')

def leave_matrix_right():
    select_current_matrix()
    actions.key('escape')

def select_current_matrix():
    actions.edit.line_start()
    actions.user.equatio_wait_movement_delay()
    actions.edit.extend_left()
    actions.user.equatio_wait_selection_delay()


def entry_move_horizontally_by_amount(amount):
    movement_action = go_to_next_matrix_entry
    if amount < 0:
        movement_action = go_to_previous_matrix_entry
    for iteration in range(abs(amount)):
        movement_action()

def compute_how_much_to_move_horizontally_to_reach_entry_given_column_count_and_target(column_count, target):
    target_row = target[0]
    target_column = target[1]
    horizontal_movement_amount = target_column - 1
    vertical_movement_amount = target_row - 1
    if vertical_movement_amount > 0:
        horizontal_movement_amount += (vertical_movement_amount)*column_count
    return horizontal_movement_amount

def get_matrix_dimensions():
    select_current_matrix()
    matrix_text = actions.user.equatio_get_selected_text()
    matrix_dimensions = MatrixDimensions(matrix_text)
    return matrix_dimensions.get_rows(), matrix_dimensions.get_columns()

class Matrix:
    COLUMN_SEPARATOR = '&'
    ROW_SEPARATOR = '\\\\'
    BEGINNING_TEXT = '\\begin{matrix}'
    ENDING_TEXT = '\\end{matrix}'
    def __init__(self, num_rows, num_columns):
        self.num_rows = num_rows
        self.matrix = {}
        self.num_columns = num_columns
        for row in range(1, self.num_rows + 1):
            for column in range(1, self.num_columns + 1):
                self.update(row, column, '')

    def update(self, row, column, value):
        self.matrix[(row, column)] = value
    def entry(self, row, column):
        return self.matrix[row, column]
    def fill_with_text(self,fill_value):
        for row in range(1, self.num_rows + 1):
            for column in range(1, self.num_columns + 1):
                self.update(row, column, fill_value)
    def text(self):
        output = Matrix.BEGINNING_TEXT
        for row in range(1,self.num_rows +1):
            for column in range(1,self.num_columns +1):
                output += self.entry(row, column)
                if column < self.num_columns: 
                    output += Matrix.COLUMN_SEPARATOR
            if row < self.num_rows: 
                output += Matrix.ROW_SEPARATOR
        output += Matrix.ENDING_TEXT
        return output

CONTAINER_BEGINNING = '\\begin'
CONTAINER_ENDING = '\\end'
TEXT_FIELD_BEGINNING = '\\text'
TEXT_FIELD_ENDING = '}'
class MatrixDimensions:
    def __init__(self, matrix_text):
        self.matrix_text = matrix_text
        self.index = 0
        self.container_depth = 0
        self.row_count = 0
        self.column_count = 0
        self.matrix_found = False
        self.count_rows_and_columns()

    def get_rows(self):
        return self.row_count
    def get_columns(self):
        return self.column_count
    
    def count_rows_and_columns(self):
        while self.count_not_finished():
            self.process_text_at_index()
        #The prior counting only counted separators, so must add one to each
        self.increase_column_count()
        self.increase_row_count()
        if not self.matrix_found:
            self.column_count = 0
            self.row_count = 0

    def count_not_finished(self):
        return self.index <= len(self.matrix_text)

    def process_text_at_index(self):
        if self.found_column_separator():
            self.handle_found_column_separator()
        elif self.found_row_separator():
            self.handle_found_row_separator()
        elif self.found_container_beginning():
            self.handle_container_beginning()
        elif self.found_container_ending():
            self.handle_container_ending()
        elif self.found_text_field():
            self.skip_text_field()
        else:
            self.advance_search_by_one_character()

    def found_column_separator(self):
        return self.text_at_index_matches(Matrix.COLUMN_SEPARATOR)
    def found_row_separator(self):
        return self.text_at_index_matches(Matrix.ROW_SEPARATOR)
    def found_container_beginning(self):
        return self.text_at_index_matches(CONTAINER_BEGINNING)
    def found_container_ending(self):
        return self.text_at_index_matches(CONTAINER_ENDING)
    def found_text_field(self):
        return self.text_at_index_matches(TEXT_FIELD_BEGINNING)

    def text_at_index_matches(self, text):
        return len(self.matrix_text) >= self.index + len(text) - 1 and self.matrix_text[self.index : self.index + len(text)] == text

    def handle_found_column_separator(self):
        if self.should_count_column_separator():
            self.increase_column_count()
        self.move_past_text(Matrix.COLUMN_SEPARATOR)
    def should_count_column_separator(self):
        #Only count column separators before the first row separator gets found to avoid adding the column separators
        #in each row to the count, which would overcount
        #Also do not count column separators with a backslash before them
        return self.row_count == 0 and self.not_inside_inner_container_or_outside_matrix() and self.not_backslash_before_index()
    def increase_column_count(self):
        self.column_count += 1
    
    def not_inside_inner_container_or_outside_matrix(self):
        return self.container_depth == 1
    def not_backslash_before_index(self):
        return self.index == 0 or not self.matrix_text[self.index - 1] == '\\'
    
    def move_past_text(self, text):
        self.index += len(text)
    
    def handle_found_row_separator(self):
        if self.should_count_row_separator():
            self.increase_row_count()
        self.move_past_text(Matrix.ROW_SEPARATOR)
    
    def should_count_row_separator(self):
        return self.not_inside_inner_container_or_outside_matrix()
    def increase_row_count(self):
        self.row_count += 1
    
    def handle_container_beginning(self):
        if self.text_at_index_matches(Matrix.BEGINNING_TEXT):
            self.matrix_found = True
        self.increase_container_depth()
        self.move_past_text(CONTAINER_BEGINNING)
    def increase_container_depth(self):
        self.container_depth += 1
    
    def handle_container_ending(self):
        self.decrease_container_depth()
        self.move_past_text(CONTAINER_ENDING)
    def decrease_container_depth(self):
        self.container_depth -= 1
    
    def skip_text_field(self):
        self.move_past_text(TEXT_FIELD_BEGINNING)
        while self.matrix_text[self.index] != TEXT_FIELD_ENDING or self.matrix_text[self.index - 1] == '\\':
            self.move_to_next_instance_of(TEXT_FIELD_ENDING)
        self.move_past_text(TEXT_FIELD_ENDING)
    def move_to_next_instance_of(self, text):
        next_instance_index = self.matrix_text.index(TEXT_FIELD_ENDING, self.index)
        self.index = next_instance_index

    def advance_search_by_one_character(self):
        self.index += 1
