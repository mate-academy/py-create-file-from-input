def main():
    name_of_file = input("Enter name of the file: ")
    file = open(f"{name_of_file}.txt", "a")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file.write(f"{content}\n")
    file.close()


if __name__ == "__main__":
    main()
