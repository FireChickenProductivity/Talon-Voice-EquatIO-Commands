# Dictating Variables
Letters are dictated using the community repository phonetic alphabet.

Greek letters can be dictated using their names except for theta, which is dictated by saying angle to improve accuracy (theta kept getting mixed up with beta and eta).

Capital english and greek letters can be dictated with Tall (letter) or Big (letter).

Because capital delta is more common in math than lower case delta, dictating delta produces upper case delta. Lower case delta is dictated as small delta.

Positive integers and letters dictated immediately after any letter other then capital delta are automatically subscripted.

Dictating flat or straight before dictating letters prevents automatic subscripting after them.

# Exponentiation
Dictating squared raises the previous character to the second power.

Dictating cubed raises the previous character to the third power.

Dictating inverse raises the previous character to the minus first power.

Dictating transpose gives the previous character the superscript T.

Dictating to the followed by an ordinal number from second, third ... through ninetyninth raises the previous character to the corresponding exponent (second gives 2, third gives 3, tenth gives 10, etc). 

Dictating the above exponentiation commands immediately after something that will be automatically subscripted will cause the exponentiation to go into the subscript.

Dictating power starts a superscript.

# Manual Subscripting
Dictating subscript, script, or sub manually starts a subscript.

# Movement Commands
who: moves the cursor to the right.

back: moves the cursor to the left.

cape: presses escape, which usually exits the current text container. Note that a normal Talon setup already has the command escape that already presses escape.

back cape or shift cape: presses shift escape, which usually exits the current text container by moving back.

out: goes to the end of the current line and then to the right. Useful for things like exiting parentheses, subscripts, and superscripts.

move: goes to the end of the current line.

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

<h2>Calculus Commands</h2>
<h3>Limits</h3>
limit: types lim and then subscripts.

goes to: produces a right arrow.

<h3>Integration</h3>
integrate: produces an integral symbol and leaves the cursor at the integral's lower bound.

integral: produces an integral symbol and moves the cursor to the right of it.

dubintegrate: produces a double integral with the cursor at the first integral's lower bound.

triple integrate: produces a triple integral with the cursor at the first integral's lower bound.

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

# Matrix Commands
<h2>Making Matrices</h2>
matrix (small positive integer) [by] (small positive integer): creates a matrix surrounded by square brackets with the number of rows specified by the first integer and the number of columns specified by the second integer.

column (a small positive integer): creates a column surrounded by square brackets with the number of rows given by the integer.

matrix column (small positive integer) [by] (small positive integer): creates a matrix built out of columns surrounded by square brackets with the number of rows given by the first integer and the number of columns given by the second integer. This is useful if you want to input entries a column at a time instead of doing it a row at a time. Note that the matrix navigation commands will treat each column as its own matrix.

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

send (a list of symbols that can be small integers, minus signs, or decimal points): inputs the symbols into the matrix and attempts to go to the next entry after each number (the cursor must not be within a text container within the matrix for it to go to the next entry properly).
