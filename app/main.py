def main():
    name = input("Enter name of the file: ")
    new_file = open(name + ".txt", "a")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            new_file.close()
            break
        new_file.write(line + "\n")


if __name__ == "__main__":
    main()
