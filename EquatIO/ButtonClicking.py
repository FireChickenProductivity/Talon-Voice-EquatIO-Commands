from talon import actions, Module
from .MousePosition import MousePositionFile, MousePosition
import os


def compute_mouse_storage_directory():
    mouse_storage_folder_name = 'positions'
    project_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(project_directory, mouse_storage_folder_name)


module = Module()

mouse_movement_delay = module.setting(
    'equatio_mouse_movement_delay',
    type = int,
    default = 0,
    desc = 'How long to pause after moving the mouse for equatio commands. Increase this if button clicking is not working for you.',
)

click_delay = module.setting(
    'equatio_click_delay',
    type = int,
    default = 200,
    desc = 'How long to pause after clicking for certain equatio commands.',
)

insert_delay = module.setting(
    'equatio_insert_delay',
    type = int,
    default = 4000,
    desc = 'How long to wait after clicking the insert math button.'
    ' Increase this if math insertion commands are not working properly but the insert math button is getting properly clicked.',
)

@module.action_class
class Actions:
    def equatio_update_insert_math_position():
        '''Stores the current mouse position as the new position of the insert math button'''
        position = get_insert_math_position()
        position.set_to_current_mouse_position()
    def equatio_update_return_position():
        '''Stores the current mouse position as the new location of the math returning click position'''
        position = get_return_position()
        position.set_to_current_mouse_position()

    def equatio_insert_math():
        '''Inserts the math'''
        position = get_insert_math_position()
        click_position(position)
        wait_insert_delay()
        return_to_math()
        wait_click_delay()
        actions.edit.select_all()

def wait_insert_delay():
    wait_delay(insert_delay)

def wait_delay(setting):
    actions.sleep(f'{setting.get()}ms')

def wait_click_delay():
    wait_delay(click_delay)

def get_insert_math_position():
    return get_position_from_name('insert math')

def get_position_from_name(name: str):
    return MousePositionFile(compute_mouse_storage_directory(), name)

# This is used to return to editing math
def get_return_position():
    return get_position_from_name('return')

def click_position(position_file: MousePositionFile):
    position = position_file.get()
    position.go()
    wait_mouse_movement_delay()
    actions.mouse_click(0)

def wait_mouse_movement_delay():
    wait_delay(mouse_movement_delay)

def return_to_math():
    position = get_return_position()
    click_position(position)
