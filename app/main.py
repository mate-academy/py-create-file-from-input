def file_creator():
    name_of_file = input("Enter name of file:")
    with open(f'{name_of_file}.txt', 'a') as f:
        while True:
            content = input("Enter new line of content:")
            if content == 'stop':
                break
            f.write(f"{content}\n")


file_creator()
