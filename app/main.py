def main() -> None:
    file_name = input("Enter name of the file: ")

    if file_name:
        with open(file_name + ".txt", "w") as text_file:
            while True:
                line = input("Enter new line of content: ")
                if line.strip() == "stop" or line.strip() == "":
                    break

                text_file.write(line + "\n")


if __name__ == "__main__":
    main()
