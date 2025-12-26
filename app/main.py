def main():
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        while True:
            texting = input('Enter new line of content: ')
            if texting == "stop":
                break
            file.write(texting + "\n")


if __name__ == "__main__":
    main()
