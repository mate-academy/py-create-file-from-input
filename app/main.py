def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.lower().endswith(".txt"):
        file_name = file_name + ".txt"
    with open(file_name, "a") as f:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            else:
                f.write(f"{line}\n")


if __name__ == "__main__":
    main()
