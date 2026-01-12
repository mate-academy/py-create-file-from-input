def main() -> None:
    file_base = input("Enter name of the file: ")
    file_name = f"{file_base}.txt"
    with open(file_name, "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
