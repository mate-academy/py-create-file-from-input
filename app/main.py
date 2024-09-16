def main():
    file_name = input('Enter name of the file: ')
    new_string = ''
    with open(file_name + '.txt', 'a') as f:
        while new_string != 'stop':
            new_string = input('Enter new line of content: ')
            if new_string != 'stop':
                f.write(new_string + '\n')
