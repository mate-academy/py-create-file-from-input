def main():
    name = input("Enter name of the file: ")
    content = input("Enter new line of content: ")
    string = f"{content}\n"
    while content != "stop":
        content = input("Enter new line of content: ")
        string += f"{content}\n"
    d = open(f"{name}.txt", "w")
    d.write(string[:-6])


if __name__ == "__main__":
    main()
