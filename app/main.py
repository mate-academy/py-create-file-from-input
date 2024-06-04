def main() -> None:
    name = input("Enter name of the file: ") + ".txt"

    with open(name, "w") as file:
        while True:
            command = input("Enter new line of content: ")
            if command == "stop":
                break
            file.write(command + "\n")
