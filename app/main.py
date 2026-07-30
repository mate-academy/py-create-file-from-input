def main() -> None:
    file_name = input("Enter name of the file: ")
    strings = []
    string = ""
    while not string == "stop" or string == "STOP":
        strings.append(string)
        string = input("Enter new line of content: ")
        if not string == "stop" or string == "":
            strings += "\n"
    strings = strings[2:]
    print(strings)
    result = "".join(strings)
    with open(f"{file_name}.txt", "w") as f:
        f.write(result)
