def main():
    name_file = input("Enter name of the file: ") + ".txt"
    with open(name_file, "a") as file:
        while True:
            write = input("Enter new line of content: ")
            if write == "stop":
                break
            file.write(write + '\n')


if __name__ == "__main__":
    main()
