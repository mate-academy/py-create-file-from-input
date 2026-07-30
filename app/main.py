def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "w") as f:
        new_line = input("Enter new line of content: ")
        while new_line != "stop":
            f.write(f"{new_line}\n")
            new_line = input("Enter new line of content: ")
