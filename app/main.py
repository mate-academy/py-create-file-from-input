def main():
    new_file = input("Enter name of the file: ")
    new_name = open(new_file + ".txt", "a")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            new_name.close()
            break
        new_name.write(new_line + "\n")


if __name__ == "__main__":
    main()
