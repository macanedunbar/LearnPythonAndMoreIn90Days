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


num_list = [1,2,3,4]
print(num_list)
for item in num_list:
    print(item)

#fib_sequence

fib_sequence = []
a, b = 0, 1
while b < 1000:
    fib_sequence.append(b)
    a,b = b, a+b

print(fib_sequence)

""" #Simple Elif Ladder
x = int(input("Enter an Integer:"))
if x < 0:
    x = 0
    print ('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print ('Single')
else:
    print('More')
"""

words = ['cat','window','defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)

print(words)

for i in range (10):
    print(i)

for i in range (0,11, 2):
    print(i)

print(list(range(5)))

primelist = []
n = 2
while n < 10:
    for x in range(2,n):
        if n % x == 0:
           # print (n, 'equals', x, '*', n//x)
            break
    else:
        primelist.append(n)
    n += 1

print(primelist)

def fib(n):
    """Fibonacci Sequence up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(2000))

def gimme_a_one():
    return 1

one = gimme_a_one()
print(one)


def f(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))

def args_to_dot_notation(*args, dotnotation = "."):
    return dotnotation.join(args)

print(args_to_dot_notation('one', 'two', 'three'))

pairs = [(1, 'one'),(2, 'two'),(3, 'three'),(4, 'four')]
print(pairs)
pairs.sort(key=lambda pair: pair[1])
print(pairs)








