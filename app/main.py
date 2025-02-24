def main() -> None:
    file_basename = input("Enter name of the file: ")
    file_name = f"{file_basename}.txt"
    file1 = open(file_name, "w")
    file1.close()

    while True:
        text_to_save = input("Enter new line of content: ")
        if text_to_save == "stop":
            break

        with open(file_name, "a") as file:
            file.write(text_to_save + "\n")


if __name__ == "__main__":
    main()
