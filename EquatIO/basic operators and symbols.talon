app: EquatIO
-

plus: '+'
negative: '-'
minus: '-'
(times|star|(inner|dot) product): '*'
# needed to override a community repository repeating command
<number_small> times: 
    user.equatio_insert_small_number(number_small)
    insert('*')
slash: '/'
(division|divide) [by]: '\\div '
#this next line is needed to properly override the knausj divide command
divide: '\\div '
#this next line is needed to properly override the knausj quotient command
quotient: '\\div '
equal: '='
equals: '='

(script|subscript|sub): '_'
(modulus|mod|percent|modulo): '%'
(pipe|absolute value|absolute): '|'
(great|greater|bigger) [than]: '>'
(less|lesser|smaller) [than]: '<'
(great|greater|bigger) [than] [or] (equals|equal) [to]: '>='
(less|lesser|smaller) [than] [or] (equals|equal) [to]: '<='
(tilde|similar [to]): '~'
circle (product|times|cross): '\\otimes '
circle dot: '\\bigodot '
(cross [product]|by): '\\times '
bang|exclaim|exclamation [point]: '!'
of: '('

summation: user.equatio_summation()
product: user.equatio_build_product()
choose|combo|combination: '\\binom '

ceiling: 
    insert('\\lceil \\rceil ')
    edit.left()
floor: 
    insert('\\lfloor \\rfloor ')
    edit.left()

vector: '\\vec '
arc: '\\overarc '
ray: '\\overrightarrow '
line: '\\overleftrightarrow '
(hat|overhead|above) tilde: '\\tilde '

(unequal|inequality|inequal): '\\ne '
(approximately|approximate|approximation|approx): '\\approx '
(proportional|proportional to|proportion): '\\propto '
congruent: '\\cong '
(square root|root|square root of): '\\sqrt '
bar: '\\bar '
hat: '\\hat '
pi: '\\pi '
delta: '\\Delta '
angle: '\\theta '

degrees:
    insert('^\\circ ')
    key(right)
plus or minus: '\\pm '
minus or plus: '\\mp '

(tangent|tan): 'tan'
sine: 'sin'
cosine: 'cos'
secant: 'sec'
cosecant: 'csc'
cotangent: 'cot'

log: 'log'
L G: 'lg'

parallel: '\\parallel '
(perpendicular|normal): '\\perpendicular '
therefore: '\\therefore '
because: '\\because '

implies: '\\Rightarrow '
(if and only if|(dub|double) (implies|implication)): '\\Longleftrightarrow '
for all: '\\forall '
[there] exists: '\\exists '
element [of]: '\\in '
[(logical|logic)] not: '\\neg '
(logical|logic|lo) and|land: '\\wedge '
[(logical|logic)] or: '\\vee '

angle (shape|symbol): '\\angle '
triangle [shape]: '\\triangle '
circle [shape]: '\\bigcirc '
square shape: '\\square '
(composed|compose|composition) [with|of] | small circle [shape]: '\\circ '

asymp|order [of] [magnitude]: '\\asymp '

(prop|proper) subset: '\\subset '
subset: '\\subseteq '
(prop|proper) (superset|soup set): '\\supset '
superset|soup set: '\\supseteq '
empty [set]: '\\varnothing '
not (in|[a] member [of]): '\\notin '
union: '\\cup '
intersect|intersection: '\\cap '

equilibrium|balance: '\\rightleftharpoons '

[the] (real|reals) [numbers]: user.equatio_paste_text('\\mathbb{{R}}')
[the] integers: user.equatio_paste_text('\\mathbb{{Z}}')
[the] (rational|rationals) [numbers]: user.equatio_paste_text('\\mathbb{{Q}}')
[the] (irrational|irrationals): user.equatio_paste_text('\\tilde{{\\mathbb{{Q}}}}')
cent|cents: '¢'
dollar|dollars: '$'

vertical [line]|vert line: '\\mid '

infinity|infinite: '\\infty '

join [op|operator]: '⋈'
assign|assignment: '\\longleftarrow '
project|projection: '\\Pi _'
select|selection: '\\sigma _'

circle plus: '\\oplus '
