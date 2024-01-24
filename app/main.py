def main():
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as new_file:
        new_file.write("")

        while True:
            line = input("Enter new line of content: ")

            if line.lower() == "stop":
                break

            new_file.write(line + "\n")


if __name__ == "__main__":
    main()
