def main() -> None:
    while True:
        file_name = input("Enter name of the file: ")
        try:
            with open(f"{file_name}.txt", "w"):
                pass
            break
        except OSError:
            print("Name Error. Try again.")
    joined_list = []
    while True:
        try:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            joined_list.append(line)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
    joined_text = "\n".join(joined_list)
    with open(f"{file_name}.txt", "w") as file:
        file.write(joined_text)


if __name__ == "__main__":
    main()
