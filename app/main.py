client_input = input('Please enter the name of file')
changed_name = client_input + '.txt'
f = open(changed_name, 'w')
while True:
    client_file_input = input('Please add some context')
    if client_file_input == 'stop':
        f.close()
        break
    f.write(client_file_input + '\n')

