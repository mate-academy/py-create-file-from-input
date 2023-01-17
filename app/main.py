def main():
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                return False
            else:
                file.write(f"{line}\n")


if __name__ == "__main__":
    main()
