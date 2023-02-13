def main() -> None:
    name = input("Enter name of the file: ") + ".txt"

    with open(name, "w") as f:
        line = ""
        while line != "stop":
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")
