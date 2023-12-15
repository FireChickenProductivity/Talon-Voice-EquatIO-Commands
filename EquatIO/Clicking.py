from talon import actions, Module, settings
from .MousePosition import MousePositionFile, MousePosition
import os


def compute_mouse_storage_directory():
    mouse_storage_folder_name = 'positions'
    project_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(project_directory, mouse_storage_folder_name)


module = Module()

mouse_movement_delay_setting_name = 'equatio_mouse_movement_delay'
mouse_movement_delay = 'user.' + mouse_movement_delay_setting_name
module.setting(
    mouse_movement_delay_setting_name,
    type = int,
    default = 500,
    desc = 'How long to pause after moving the mouse for equatio commands. Increase this if button clicking is not working for you.',
)

click_delay_setting_name = 'equatio_click_delay'
click_delay = 'user.' + click_delay_setting_name
module.setting(
    click_delay_setting_name,
    type = int,
    default = 200,
    desc = 'How long to pause after clicking for certain equatio commands.',
)

insert_delay_setting_name = 'equatio_insert_delay'
insert_delay = 'user.' + insert_delay_setting_name
module.setting(
    insert_delay_setting_name,
    type = int,
    default = 4000,
    desc = 'How long to wait after clicking the insert math button.'
    ' Increase this if math insertion commands are not working properly but the insert math button is getting properly clicked.',
)

edit_delay_setting_name = 'equatio_edit_delay'
edit_delay = 'user.' + edit_delay_setting_name
module.setting(
    edit_delay_setting_name,
    type = int,
    default = 2000,
    desc = 'How long to wait after clicking the edit math button.'
    ' Increase this if math edit commands are not working properly but the edit math button is getting properly clicked.',
)

desmos_browser_setting_name = 'equatio_desmos_browser'
desmos_browser = 'user.' + desmos_browser_setting_name
module.setting(
    desmos_browser_setting_name,
    type = str,
    default = 'edge',
    desc = 'Used with the knausj focus action to try to bring up the browser with desmos'
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

    def equatio_update_edit_math_position():
        '''Stores the current mouse position as the location of the edit math button'''
        position = get_edit_math_position()
        position.set_to_current_mouse_position()

    def equatio_update_equation_editor_position():
        '''Stores the current mouse position as the location of the equation editor button'''
        position = get_equation_editor_position()
        position.set_to_current_mouse_position()
    
    def equatio_update_desmos_position():
        '''Stores the current mouse position as the place to click when returning to the desmos calculator'''
        position = get_desmos_position()
        position.set_to_current_mouse_position()


    def equatio_insert_math():
        '''Inserts the math'''
        position = get_insert_math_position()
        click_position(position)
        wait_insert_delay()
        return_to_math()
        wait_click_delay()
        actions.edit.select_all()
    
    def equatio_insert_saved_word_math():
        '''Inserts the math into word and saves it'''
        position = get_insert_math_position()
        click_position(position)
        actions.user.switcher_focus('word')
        wait_insert_delay()
        actions.edit.save()
        return_to_math()
        wait_click_delay()
        actions.edit.select_all()

    def equatio_edit_math():
        '''Click the edit math button'''
        position = get_edit_math_position()
        click_position(position)
        wait_edit_delay()
        return_to_math()

    
    def equatio_click_equation_editor():
        '''Clicks the equation editor'''
        position = get_equation_editor_position()
        click_position(position)
    
    def equatio_return_math():
        '''Clicks on the return math position'''
        position = get_return_position()
        click_position(position)
    
    def equatio_switch_to_desmos():
        '''Brings up the desmos calculator in the configured browser'''
        focus_desmos_browser()
        position = get_desmos_position()
        click_position(position)

def focus_desmos_browser():
    actions.user.switcher_focus(settings.get(desmos_browser))

def wait_insert_delay():
    wait_delay(insert_delay)

def wait_delay(setting):
    wait_milliseconds(settings.get(setting))

def wait_milliseconds(time: int):
    actions.sleep(f'{time}ms')

def wait_click_delay():
    wait_delay(click_delay)

def wait_edit_delay():
    wait_delay(edit_delay)

def get_insert_math_position():
    return get_position_from_name('insert math')

def get_position_from_name(name: str):
    return MousePositionFile(compute_mouse_storage_directory(), name)

# This is used to return to editing math
def get_return_position():
    return get_position_from_name('return')

def get_edit_math_position():
    return get_position_from_name('edit math')

def get_equation_editor_position():
    return get_position_from_name('equation editor')

def get_desmos_position():
    return get_position_from_name('desmos')

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
