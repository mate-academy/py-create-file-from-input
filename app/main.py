def file_creator():
    print("Enter name of file:")
    name_of_file = input()
    with open(f'{name_of_file}.txt', 'a') as f:
        while True:
            print("Enter new line of content:")
            content = input()
            if content == 'stop':
                break
            f.write(f"{content}\n")


file_creator()
