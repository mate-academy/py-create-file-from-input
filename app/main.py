def main():
    name = input("Enter name of the file: ")
    name += '.txt'
    with open(name, "a") as f:
        next_line = input("Enter new line of content: ")
        while next_line != "stop":
            f.write(f"{next_line}\n")
            next_line = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
