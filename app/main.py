def main() -> None:
    name = str(input("Enter name of the file: ")) + ".txt"
    with open(name, "a") as file:
        while True:
            stop = input("Enter new line of content: ")
            if stop == "stop":
                break
            else:
                file.write(stop + "\n")
