def main():
    name = input("Enter name of the file: ")
    with open(name + ".txt", "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content != "stop":
                file.write(content)
            else:
                return


if __name__ == "__main__":
    main()