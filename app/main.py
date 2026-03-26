def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            write_text = input("Enter new line of content: ")
            if write_text == "stop":
                break
            file.write(f"{write_text}\n")


if __name__ == "__main__":
    main()
