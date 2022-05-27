file_name = input("Please, enter File name : ")

with open(f"{file_name}.txt", "w", encoding="utf8") as file:
    line = ""
    while line != "stop":
        line = input('Enter new line of content: ')
        file.write(f"{line}\n")
