def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as new_file:
        stop = False
        while not stop:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                stop = True
            else:
                new_file.write(f"{new_line}\n")
