def main():
    name = input("Enter name of the file: ")
    message = input("Enter new line of content: ")
    with open(f"{name}.txt", "a") as file:
        while message != "stop":
            file.write(f"{message}\n")
            message = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
