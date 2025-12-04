def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:
        while True:
            new_line = input("Enter new line of content: ")

            if new_line == "stop":
                break
            else:
                file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
