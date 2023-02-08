# Dictating Variables
Letters are dictated using the community repository phonetic alphabet.

Greek letters can be dictated using their names except for theta, which is dictated by saying angle to improve accuracy (theta kept getting mixed up with beta and eta).

Capital english and greek letters can be dictated with Tall (letter) or Big (letter).

Because capital delta is more common in math than lower case delta, dictating delta produces upper case delta. Lower case delta is dictated as small delta.

There are three subscripting settings: automatic, automatic numbers, and manual. Regardless of which setting is active, dictating flat or straight before dictating letters prevents automatic subscripting of letters after them but will subscript subsequent numbers (including numbers immediately after exponentiation that was dictated immediately after letters).

<h2>Automatic Subscript Setting Rules</h2>

Positive integers and letters dictated immediately after the dictation of any letter other than capital delta are automatically subscripted.

Positive integers and letters dictated immediately after any exponent dictated immediately after the dictation of any letter other than capital delta are also automatically subscripted.

<h2>Automatic Numbers Subscript Setting Rules</h2>
Positive integers dictated immediately after the dictation of any letter or after any exponent dictated immediately after any letter are automatically subscripted.

<h2>Manual Subscript Setting</h2>
No automatic subscripting

<h2>Changing the Subscript Setting</h2>
The active subscript setting can be changed by dictating "subscript setting" followed by the desired subscript setting name. The word auto can be used instead of automatic (so you can say subscript setting auto and subscript setting auto numbers).

The default subscript setting upon launching talon can be changed by changing the user.equatio_default_subscript_setting in the settings.talon file. To do this, go to the setting in the file and change the text in single quotation marks to the name of the desired mode in all lower case.

# Exponentiation
Dictating squared raises the previous character to the second power.

Dictating cubed raises the previous character to the third power.

Dictating inverse raises the previous character to the minus first power.

Dictating transpose gives the previous character the superscript T.

Dictating to the followed by an ordinal number from second, third ... through ninetyninth raises the previous character to the corresponding exponent (second gives 2, third gives 3, tenth gives 10, etc). 

Dictating the above exponentiation commands immediately after something that will be automatically subscripted will cause the exponentiation to go into the subscript.

Dictating power starts a superscript.

Dictating poof starts a subscript in parentheses (poof is short for power of).

Dictating poof (transpose or pose): starts a superscript in parentheses with the parentheses followed by the transpose symbol.

Dictating puff (small positive integer) raises the previous character to that integer in parentheses.

Dictating puff (transpose or pose) (small nonnegative integer): raises the previous character to that integer in parentheses and transposed.

# Manual Subscripting
Dictating subscript, script, or sub manually starts a subscript.

# Movement Commands
who: moves the cursor to the right.

pass: moves the cursor to the right twice.

cape: presses escape, which usually exits the current text container. Note that a normal Talon setup already has the command escape that already presses escape.

back cape or shift cape: presses shift escape, which usually exits the current text container by moving back.

out: goes to the end of the current line and then to the right. Useful for things like exiting parentheses, subscripts, and superscripts.

leave or leaf: does the same thing as out twice.

move: goes to the end of the current line.

<h2>Movement With Operator Commands</h2>
The following commands move to the right and input the specified symbol:

rush: +

rine: -

rhyme or rhymes: *

ross: the cross multiplication sign

rash: /

reek or re quill or reeks or re quills or requal or requals: =

# Symbol Commands
stuff in square brackets is optional

<h2>Operator Commands</h2>

plus: +

minus or negative: -

times or star or inner product or dot product: dot multiplication symbol

cross [product] or by: cross multiplication symbol

slash: / (starts division)

division [by] or divide [by] or quotient: division symbol

equal or equals: =

unequal or inequality or inequal: inequality symbol

approximately or approximate or approximation or approx: approximation symbol

proportional or proportional to or proportion: proportional to symbol

congruent: congruent to symbol

modulus or mod or percent or modulo: %

pipe or absolute value or absolute: starts absolute value

great [than] or greater [than] or bigger [than]: >

less [than] or lesser [than] or smaller [than]: <

(great or greater or bigger) [than] [or] (equals or equal) [to]: greater than or equal to sign

(less or lesser or smaller) [than] [or] (equals or equal) [to]: less than or equal to sign

tilde or similar [to]: ~

circle (product or times or cross): cross multiplication sign within a circle

circle dot: dot multiplication sign within a circle

bang or exclaim or exclamation [point]: !

summation: summation operator

product: product operator (not the multiplication sign)

choose or combo or combination: creates a parenthesized container that can hold two rows of math (used for things like n choose k)

ceilling: ceiling function

floor: floor function

(compose or composed or composition) [with or of] or small circle [shape]: function composition symbol

asymp or order [of] [magnitude]: order of magnitude symbol

equilibrium or balance: equilibrium symbol

square root or root or square root of: square root symbol

plus or minus: plus or minus symbol

minus or plus: minus or plus symbol

<h2>Logical Operator Commands</h2>
[logical or logic] not: not symbol

(logical or logic or lo) and or land: and symbol

(logical or logic) or: or symbol

implies: implication symbol

if and only if or (dub or double) (implies or implication): double implication symbol

for all: for all symbol (upside down A)

[there] exists: there exists symbol (backwards E)

therefore: therefore symbol

because: because symbol

<h2>Set Notation Commands</h2>
element [of]: element of symbol

(prop or proper) subset: proper subset symbol

subset: subset symbol

superset or soup set: superset symbol

empty [set]: empty set symbol

not (in or [a] member [of]): not an element of the set symbol

union: union symbol

intersect or intersection: intersection symbol

<h2>Number Set Commands</h2>
[the] (real or reals) [numbers]: the real numbers symbol

[the] integers: the integers symbol

[the] (rational or rationals) [numbers]: the rational numbers symbol

[the] (irrational or irrationals): the irrational numbers symbol

<h2>Geometry Symbol Commands</h2>
parallel: parallel symbol

perpendicular or normal: perpendicular symbol

angle (shape or symbol): a symbol representing an angle

triangle [shape]: creates a triangle shaped symbol

circle [circle]: creates a circle shaped symbol

square shape: creates a square shaped symbol

ray: creates the ray overhead symbol

vector: creates the vector overhead symbol

arc: creates the arc overhead symbol

line: creates the line overhead symbol

(hat or overhead or above) tilde: creates the overhead tilde symbol

<h2>Miscellaneous Symbol Commands</h2>
dollar or dollars: $

cent or cents: ¢

vertical [line] or vert line: creates a small vertical line

infinity or infinite: infinity symbol

norm: norm symbol

norm (small nonnegative integer): the specified integer norm

norm (infinity or infinite): the infinity norm

join [op or operator]: the relational algebra join operator

assign or assignment: the relational algebra assignment operator

project or projection: the relational algebra projection operator plus subscript

select or selection: the relational algebra selection operator plus subscript

circle plus: a plus sign in a circle

<h2>Calculus Commands</h2>
<h3>Limits</h3>
limit: types lim and then subscripts.

goes to: produces a right arrow.

<h3>Integration</h3>
integrate: produces an integral symbol and leaves the cursor at the integral's lower bound.

integral: produces an integral symbol and moves the cursor to the right of it.

[(dub or double or triple)] (integrate or integral): the first part determines the number of integrals. If the first part is ignored, the command produces a single integral. If the first part is dub or double, the command produces a double integral. If the first part is triple, the command produces a triple integral. The second part determines whether the cursor should move to the right of the integrals or will be placed at the first integral's lower bound. Integral means moving to the right while integrate means moving to the first integral's lower bound.

[(dub or double or triple)] (integrate or integral) (with or of) [respect to] (a list of letters): the same as the previous command but puts parentheses followed by the list of letters with d before each letter after the integrals.

(integrate or integration or integral or from) line: produces a vertical dashed line with a subscript and superscript to denote from the subscript value to the superscript value (it would be better to produce a line that was not dashed, which is conventional, but EquatIO does not currently provide that capability). The cursor starts out within the subscript.

<h3>Differentiation</h3>
prime: creates the prime symbol. If used immediately after something that will be automatically subscripted, then the prime symbol will be created within the subscript.

partial or part: creates the partial differential symbol.

derive: types out d/d.

derive [order or by] (small positive integer): similar to derive but raises each d to the power of the small positive integer.

derive [order or by] (small positive integer) of (letter): similar to the command above but puts the letter after the second d and then exits the fraction.

(partial or part) (derive or drive or rive): similar to derive but produces the partial differential symbol instead of the d's.

(partial or part) (derive or drive or rive) [order or by] (small positive integer): similar to the above command but exponentiates the partial differential symbols by the small positive integer.

(partial or part) (derive or drive or rive) [order or by] (small positive engager) of (letter): similar to the above command but puts the letter after the second partial differential symbol and then exits the fraction.

# Trigonometry Commands
tangent or tan: tan

sine: sin

cosine: cos

secant: sec

cosecant: csc

cotangent: cot

degrees: creates the degrees symbol

# Logarithm Commands
log: log

L G: lg

# Matrix Commands
<h2>Making Matrices</h2>
(matrix or mat) (small positive integer) [by] (small positive integer): creates a matrix surrounded by square brackets with the number of rows specified by the first integer and the number of columns specified by the second integer.

column (a small positive integer): creates a column surrounded by square brackets with the number of rows given by the integer.

(matrix or mat) column (small positive integer) [by] (small positive integer): creates a matrix built out of columns surrounded by square brackets with the number of rows given by the first integer and the number of columns given by the second integer. This is useful if you want to input entries a column at a time instead of doing it a row at a time. Note that the matrix navigation commands will treat each column as its own matrix.

By dictating the name of a matrix container in one of those commands before the first positive integer, those commands will use that container in place of the standard square brackets. Options currently include pipe or bar for vertical lines, pipes or bars for double vertical lines, brace for curly braces, paren for parentheses, and square or bracket for the standard square brackets.

[(matrix or mat)] augment (small positive integer) [by] (small positive integer): augments the current matrix with an empty additional matrix with the specified dimensions. Assumes that the cursor is to the right of the matrix to augment but within its container (the container is the stuff around the matrix, such as square brackets, parentheses, etc). The first integer gives the number of rows and the second integer gives the number of columns.

[(matrix or mat)] augment (small positive integer): same as the previous command but uses 1 as the number of columns.

<h2>Navigating Matrices</h2>
The following movement commands assume that the cursor is within a matrix entry and not within another text container.

[go or move or matrix] entry (a small positive integer) (a small positive integer): goes to the entry at the row specified by the first positive integer and the column given by the second positive integer.

[go or move or matrix] first entry: goes to the first entry of the matrix.

[go or move or matrix] last entry: goes to the last entry of the matrix.

[go or move or matrix] next entry: goes to the next entry of the matrix.

[go or move or matrix] (previous or back): goes to the previous entry of the matrix.

<h2>Miscellaneous</h2>
new column: creates a new column if within matrix.

leave matrix left: leaves the matrix and goes to the left.

leave matrix right: leaves the matrix and goes to the right. Unfortunately, this command only moves to the right of the innermost container of the matrix, so using this command with a matrix with multiple containers (such as multiple parentheses, lines, or square brackets) does not completely get you out of the matrix.

send (a list of symbols that can be small integers, minus signs, or decimal points): inputs the symbols into the matrix and attempts to go to the next entry after each number (the cursor must not be within a text container within the matrix for it to go to the next entry properly). This command additionally interprets "oh" as the number zero. 

toss (a list of symbols that can be small integers, minus signs, or decimal points): the same as send but presses right twice at the end instead of only once.

# Button Usage and Clicking Commands

This set up includes commands for pressing buttons provided that the user runs commands that will tell it where the buttons are. Dictating "update insert math" will tell the system that the insert math button is located at the cursor's current position. Dictating "update math return" will tell the system that the cursor's current position is the position to click on to return to editing math. Dictating "update equation editor" tells the system that the cursor's current position is the position to click on to toggle the equation editor. Dictating "update edit math" tells the system that the cursor's current position is the position of the edit math button.

The following commands can be used after the mouse positions are properly configured:

Dictating "insert math" will click the insert math button, then click back into the editor, and then select the text.

Dictating "math save" will perform the same actions as the insert math command but will also switch to the word document that the math is being inserted into and save the math after it gets inserted before clicking back into the editor.

Dictating "equatio edit" will click the edit math button and then, after a pause, click back into the editor. This command can be used even when equatio is not the current application or is even not running.

Dictating "equatio editor" or "equatio equation editor" will click the equation editor button. This command can be used even when equatio is not the current application or is even not running.

Dictating "math return" will click the math return position even if equatio is not the current application or not running.

# Switching to Desmos Calculator

To switch to the desmos calculator (or another browser based calculator) currently open, use the update desmos command to configure the mouse position to click on to make the calculator app active and configure the equatio_desmos_browser setting so that the knausj focus action can bring up your desired browser. Then use the desmos command from equatio.

# Text Field Commands
text: creates a text field

text dictate: creates a text field and switches to dictation mode

text window: creates a text field, switches to dictation mode, and opens the draft window

finish: if in equatio and dictation mode, switches to command mode and exits the text field. If using the dragon speech engine with talon in equatio and not in command mode, the command switches to talon mode and exits the text field. This command is anchored (cannot be chained with other commands).

Dragon text: if using the dragon speech engine with talon, this will insert a text field and activate dragon mode. This command is anchored (cannot be chained).



# Settings
Settings can be adjusted in the settings.talon file.

The user.equatio_selection_delay setting determines how long in milliseconds commands will pause after selecting text. Try increasing this if commands that select text are not working.

The user.equatio_clipboard_operation_delay setting determines how long in milliseconds commands will pause when using the clipboard. Try increasing this if commands that use the clipboard are not working.

The user.equatio_movement_delay setting determines how long in milliseconds commands will pause after performing certain kinds of movements. If some commands involving movement do not work, try increasing this.

The user.equatio_default_subscript_setting setting is described above in the discussion of subscript settings.

The user.equatio_desmos_browser setting determines which browser the desmos command will switch to. The setting should give a name that the knausj focus action can recognize.

<h2>Button Usage Delay Settings</h2>
The user.equatio_mouse_movement_delay setting determines how long in milliseconds commands should pause after moving the mouse. Try increasing this if any mouse commands are not working.


The user.equatio_click_delay setting determines how long in milliseconds certain commands will pause after clicking to give time for the application to finish processing the click. If a mouse command does something too soon after clicking for it to work, try increasing this.

The user.equatio_insert_delay setting determines how long to wait in milliseconds for equatio to finish inserting math. If any commands do not wait long enough for equatio to finish inputting math to work properly, try increasing this.

The user.equatio_edit_delay setting determines how long to wait in milliseconds for equatio to finish loading math after clicking the edit math button. Try increasing this if any commands do not wait long enough for equatio to finish loading math to edit.
