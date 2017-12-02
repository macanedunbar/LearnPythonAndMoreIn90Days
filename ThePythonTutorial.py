# The Python Tutorial From Python.org. Example Code
# being retyped and analyzed to see how it works.


print('string')
print('\'string')
print('\"string\"')
print('"string"')
print('"Isn\'t," she said.')

#notice space at end due to '\' at end ** quirk
print(r'C:\this\path\is\rawtext\ ')

#multiple line string literal
print("""\
Usage: Thingy [Options]
    -h                       Display this usage message
    -H hostname              Hostname to connect to
""", end="")

print("~~~~~notice space after this~~~~~")

print("""
Usage: Thingy [Options]
    -h                       Display this usage message
    -H hostname              Hostname to connect to
""")

text = 'these ' 'join'
print(text)
text2 = ('these also'
' join')
print(text2)

repeater = 3 * "repeat" + " ADDED repeat"
print(repeater)

print("firstrepeat: ", repeater[0:6])

text3 = "dude"
print(text3[:])
print("bro" + text3[:])
print("broo" + text3[2:3])
print(len("broo" + text3[2:3]))
























