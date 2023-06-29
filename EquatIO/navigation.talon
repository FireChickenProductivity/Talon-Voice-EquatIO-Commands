app: EquatIO
-

out:
    edit.line_end()
    edit.right()

leave|leaf:
    edit.line_end()
    edit.right()
    edit.line_end()
    edit.right()

move:
    edit.line_end()

who:
    edit.right()

pass:
    edit.right()
    repeat(1)

cape:
    key(escape)

(back|shift) cape:
    key(shift-escape)
    

#movement and operator commands
rush:
    edit.right()
    insert('+')

rine:
    edit.right()
    insert('-')

rhyme|rhymes:
    edit.right()
    insert('*')
ross:
    edit.right()
    insert('\\times ')


rash:
    edit.right()
    insert('/')

reek|re quill|reeks|re quills|requal|requals:
    edit.right()
    insert('=')

rough:
    edit.right()
    insert('()')
    edit.left()
