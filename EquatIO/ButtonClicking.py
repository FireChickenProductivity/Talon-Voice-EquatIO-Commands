from talon import actions, Module
from .MousePosition import MousePositionFile, MousePosition
import os


def compute_mouse_storage_directory():
    mouse_storage_folder_name = 'positions'
    project_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(project_directory, mouse_storage_folder_name)


module = Module()
@module.action_class
class Actions:
    def equatio_update_insert_math_position():
        '''Stores the current mouse position as the new position of the insert math button'''
        position = get_insert_math_position()
        position.set_to_current_mouse_position()
    def equatio_insert_math():
        '''Inserts the math'''
        position = get_insert_math_position()
        click_button(position)


def get_insert_math_position():
    return MousePositionFile(compute_mouse_storage_directory(), 'insert math')

def click_button(position_file: MousePositionFile):
    position = position_file.get()
    position.go()
    wait_mouse_movement_delay()
    actions.mouse_click(0)

def wait_mouse_movement_delay():
    actions.sleep('100ms')