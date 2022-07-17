def main():
    name_of_file = input("Enter name of the file: ") + ".txt"
    while True:
        with open(name_of_file, "a") as f:
            container = input("Enter new line of content: ")
            if container != "stop":
                f.write(container + "\n")
            else:
                break


if __name__ == "__main__":
    main()
