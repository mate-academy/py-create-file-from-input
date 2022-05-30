a = input('Please enter the name of file')
c = a + '.txt'
f = open(c, 'w')
while True:
    b = input('Please add some context')
    if b == 'stop':
        break
    f.write(b)
    f.write(' ')
