
def main():
    client_input = input('Enter name of the file: ')
    changed_name = client_input + '.txt'
    f = open(changed_name, 'w')
    while True:
        client_file_input = input('Enter new line of content: ')
        if client_file_input == 'stop':
            f.close()
            break
        f.write(client_file_input + '\n')
