def create_a_file():
    name_of_file = input("Please, enter the file name: ")
    name_of_file = name_of_file + ".txt"
    with open(name_of_file, "w") as file:
        while True:
            line = input('Please, enter the line of the content '
                         'or "stop" for stop the program: ')
            if line == "stop":
                print("Stopped")
                break
            file.write(line + "\n")
