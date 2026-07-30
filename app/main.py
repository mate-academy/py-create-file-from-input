def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        while True:
            info_input = input("Enter new line of content: ")
            if info_input == "stop":
                break
            file.write(f"{info_input}\n")


if __name__ == "__main__":
    main()
