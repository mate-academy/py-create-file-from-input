def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name = file_name + ".txt"
    with open(f"{file_name}", "w") as f:
        while True:
            tekst = input("Enter new line of content: ")
            if tekst == "stop":
                break
            f.write(tekst + "\n")


if __name__ == "__main__":
    main()
