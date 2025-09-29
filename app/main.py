def main() -> None:
    file_name = str(input("Enter name of the file: "))
    with open(f"{file_name}.txt", "w") as f:
        f.write(f"{file_name}\n")
        while True:
            content = str(input("Enter new line of content: "))
            if content.lower() != "stop":
                f.write(f"{content}\n")
            else:
                break


if __name__ == "__main__":
    main()
