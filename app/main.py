def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            new_input = input("Enter new line of content: ")
            if new_input == "stop".lower():
                break
            f.write(f"{new_input}\n")


if __name__ == "__main__":
    main()
