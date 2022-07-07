app: EquatIO
-

out:
    edit.line_end()
    edit.right()

move:
    edit.line_end()

back:
    edit.left()

who:
    edit.right()

cape:
    key(escape)

(back|shift) cape:
    key(shift-escape)