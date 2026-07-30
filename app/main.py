def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    print(file_name)
    with open(file_name, "w") as f:
        while True:
            written = input("Enter new line of content: ")
            if written.lower() == "stop":
                break
            f.write(f"{written}" + "\n")


if __name__ == "__main__":
    main()
